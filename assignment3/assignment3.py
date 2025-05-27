#=====================================================================
#Task 1
import pandas as pd

#part 1

data = {
    'Name': ['Alice', 'Bob', 'charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

into_df = pd.DataFrame(data)
print(into_df)
task1_data_frame = into_df  # save the DataFrame in a variable called task1_data_frame


#part 2:
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)


#part 3:
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print(task1_older)


#part 4:
task1_older.to_csv('employees.csv', index=False)

#=====================================================================

#Task 2

#Part 1: 

task2_employees = pd.read_csv('employees.csv')
print(task2_employees)


#part 2: 
import json 

json_employees = pd.read_json('additional_employees.json')
print(json_employees)

#part 3: 

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print (more_employees)


#=====================================================================

# Task 3: 

#part 1
first_three = more_employees.head(3)
print(first_three)


#part 2
last_two = more_employees.tail(2)
print(last_two)

#part 3: 
employee_shape = more_employees.shape

#part 4: 
more_employees.info()

#=====================================================================

#Task 4: Data Cleaning

#part 1: 
dirty_data = pd.read_csv("dirty_data.csv")
clean_data = dirty_data.copy()

#part 2: 
clean_data = clean_data.drop_duplicates()
print(clean_data)

#part 3: 
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors = "coerce" )
print(clean_data["Age"])

#part 4: 
#print(clean_data)

clean_data["Salary"] = clean_data["Salary"].replace(['unknown', 'n/a'], "NaN")
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors = "coerce" )
print(clean_data)

# part 5: 
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
print(clean_data["Age"])

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print(clean_data["Salary"])

#Part 6: 
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors = "coerce")
print(clean_data["Hire Date"])

#Part 7: 

clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip()

clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.upper()
print(clean_data)