import csv
#Task 2

def read_employees():
    empty_dict = {}     # dict for keys are requested
    empty_list = []     # List to store the rows

    try:
        with open("../csv/employees.csv", newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if "fields" not in empty_dict:  # Usiong #fields to take to unoffical counting numbers
                    empty_dict["fields"] = row  # the first row ->headers
                else:
                    empty_list.append(row)     # will Store th rest of rows, except for 1
            empty_dict["rows"] = empty_list     # rows in dict
        return empty_dict

    except Exception as e:  # Copy and pasted from task 1
        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")
        

#test
employees = read_employees()
#print(employees)

###########################################################################

#Task 3

def column_index(column_name : str):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

###########################################################################

#Task 4

def first_name(row_num: int):
    to_row = employees["rows"][row_num]   # getting the row number from the from the input argument
    to_columns = column_index("first_name")  # This will take the first columns because its first_name
    return to_row[to_columns]   # from the row, take the specific columns "Firstname"

###########################################################################

#Task 5

def employee_find (employee_id: int):
    def employee_match(row):   # copy from task -> OIt take the row and give the employee id?
        return int(row[employee_id_column]) == employee_id

    matches=list(filter(employee_match, employees["rows"]))
    return matches

###########################################################################

#Task 6

def employee_find_2 (employee_id: int):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

###########################################################################

#Task 7

def sort_by_last_name():
    to_columns = column_index("last_name")
    employees["rows"].sort(key = lambda row: row[to_columns])

    return employees["rows"]

###########################################################################

#Task 8

#print(employees["fields"]) # output = ['employee_id', 'first_name', 'last_name', 'phone']
def employee_dict(row):
    empty_dict = {}  # this will be return after stuff is added in.
    fields = employees["fields"] # Take in the rows from input 
    for i in range(len(fields)):
        if fields [i] != "employee_id":
            empty_dict[fields[i]] = row[i]  # This will add the vraibles that are not employee_id into empty_dict
    return empty_dict

###########################################################################

#Task 9
def all_employees_dict():
    return_dict = {}
    for row in employees['rows']:   # Will look through all rows of employee
        return_dict[row[0]] = employee_dict(row) # The Row[0] is employee_Id, and calling Task 8 to get employee information and add it to dict.
    return return_dict


###########################################################################

#Task 10
import os

def get_this_value():
    return os.getenv("THISVALUE")



###########################################################################

#Task 11
import custom_module

def set_that_secret(secret):
    custom_module.set_secret(secret)

set_that_secret ("my_secret_code")
print(custom_module.secret)

###########################################################################

#Task 12

import csv

def read_minutes():
    with open('../csv/minutes1.csv', newline='') as file1:
        reader = csv.DictReader(file1)
        fields = reader.fieldnames
        rows = []
        for row in reader:   # Loop throw all rows in readers
            row_values = []
            for f in fields:  # Inside add all rows value, then turn it into turple
                row_values.append(row[f])
            my_tuple = tuple(row_values)
            rows.append(my_tuple)
        minutes1 = {'fields': fields, 'rows': rows} 
    
    with open('../csv/minutes2.csv', newline='') as file2:
        reader = csv.DictReader(file2)
        fields = reader.fieldnames
        rows = []
        for row in reader:
            row_values = []
            for f in fields:
                row_values.append(row[f])
            my_tuple = tuple(row_values)
            rows.append(my_tuple)
        minutes2 = {'fields': fields, 'rows': rows} 

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)

###########################################################################

#Task 13

def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    set1.update(set2)  # combining set1 and set2 together
    combination =  set1
    return combination

minutes_set = create_minutes_set() #Call the function within your assignment2.py script.  Store the value returned in the global variable minutes_set.


###########################################################################

#Task 14
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    converted = []
    for item in minutes_list: # loops though list of minutes, then take name, convert name and add all to return
        name = item[0]
        date = datetime.strptime(item[1], "%B %d, %Y") #convert x[1] using datetime.strptime
        converted.append((name, date))
    return converted

minutes_list = create_minutes_list()
print(minutes_list)


###########################################################################

#Task 15

def write_sorted_list():
    sort_list = sorted(minutes_list, key = lambda x: x[1]) # sorting based on time which is the second key

    conversion = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sort_list))  
    with open('./minutes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)  # as instructed
        writer.writerow(minutes1['fields']) #The first row you write should be the value of fields the from minutes1 dict.

        #writing over each row
        for i in conversion: 
            writer.writerow(i)
    return conversion

written_list = write_sorted_list()
print(written_list)
