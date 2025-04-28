import sqlite3
import os



def connect_database():
    os.makedirs("../db", exist_ok=True)
    
    try:
        #### TASK 1
        connection = sqlite3.connect("../db/magazines.db")
        connection.execute("PRAGMA foreign_keys = 1")   # Task 3 Step 1
        cursor = connection.cursor()
        print("Database connected successfully.")



        #### TASK 2
        #cursor.execute("PRAGMA foreign_keys = ON;") # Used for Task 2
        
        #Publishers
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        # Magazines
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
        )
        """)

        # Subscribers
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            address TEXT NOT NULL
        )
        """)

        # Subscriptions
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
        )
        """)

        print("Tables created successfully.")


        '''
        ~~~~Added to check to see if code work~~~~~

        #cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #tables = cursor.fetchall()

        #print("Tables in the database:")
        #for table in tables:
        #    print(table[0])
        '''
        return connection, cursor

    except sqlite3.Error as e:
        print(f"An error occurred while connecting: {e}")
        return None, None

    ### ~~~~ Done for Task 1~~~~~
    #finally: # need to close connection   
    #    if connection:
    #        connection.close()
    #        print("Database connection closed.")



#Task 3

def add_publisher(cursor, connection, name):
    try: 
        cursor.execute("SELECT publisher_id FROM Publishers WHERE name = ?", (name,)) #Look at publiser_id
        # If there is no ID, then insert it, else its already exist
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
            print(f"Publisher '{name}' added.")
        else: 
            print(f"Publisher '{name}' already exists.")
    except sqlite3.Error as e:
        print(f"Error adding publisher: {e}")

def add_magazine (name, publisher_id):
    try: 
        cursor.execute("SELECT magazine_id FROM Magazines WHERE name = ?", (name,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
            print(f"Magazine '{name}' added.")
        else:
            print(f"Magazine '{name}' already exists.")
    except sqlite3.Error as e:
        print(f"Error adding publisher: {e}")

def add_subscriber(name, address):
    try: 
        cursor.execute("SELECT subscriber_id FROM Subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?, ?)", (name, address))
            print(f"Subscriber '{name}' at '{address}' added.")
        else:
            print(f"Subscriber '{name}' at '{address}' already exists.")
    except sqlite3.Error as e:
            print(f"Error adding subscriber: {e}")

def add_subscription(subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("""
            SELECT subscription_id FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?
            """, (subscriber_id, magazine_id))
        if cursor.fetchone() is None:
            cursor.execute("""
                INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
                """, (subscriber_id, magazine_id, expiration_date))
            print(f"Subscription added for subscriber {subscriber_id} to magazine {magazine_id} and expiration date is {expiration_date}.")
        else:
            print(f"Subscription already exists for subscriber {subscriber_id} to magazine {magazine_id} and expiration date is {expiration_date}.")
    except sqlite3.Error as e:
            print(f"Error adding subscription: {e}")
        


#Task 4: Write SQL Queries
def information_retrieval(cursor):
    cursor.execute("SELECT * FROM Subscribers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def magazines_sorted (cursor):
    cursor.execute("SELECT * FROM Magazines ORDER BY name ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def magazines_by_publisher (cursor, publisher_name):
    cursor.execute("""
    SELECT Magazines.name 
    FROM Magazines
    JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id
    WHERE Publishers.name = ?
    """, (publisher_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)



if __name__ == "__main__":
    connection, cursor = connect_database()  #Get connection and cusor from previous function

    if connection is not None and cursor is not None:
        add_publisher(cursor, connection, "Vy Vo")
        #add_publisher(cursor, connection, "Vy Vo")  # Checking to make sure else statement works
        add_publisher(cursor, connection, "Killian Carson")
        add_publisher(cursor, connection, "Glyndon King")

        add_magazine("The New York Time", 1)
        add_magazine("Time Magazine", 2)
        add_magazine("Washington Post", 3)

        add_subscriber("Davis Unit", "1 Shields Ave, Davis, CA 95616")
        add_subscriber("Nikolai Sokolov", "221B Baker Street")
        add_subscriber("Brandon King", "221A Baker Street")

        add_subscription(1, 1, "2025-04-27")
        add_subscription(2, 2, "2025-04-26")
        add_subscription(3, 3, "2025-04-28")

        connection.commit()

        #For Task 4:
        information_retrieval (cursor)
        magazines_sorted (cursor)
        magazines_by_publisher (cursor, "Vy Vo") # using as an example

        connection.close()