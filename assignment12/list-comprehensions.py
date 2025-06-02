import pandas as pd 

df = pd.read_csv("../csv/employees.csv")
#print(df)

full_name_list = []

for i, row in df.iterrows():
    first = row["first_name"]
    last = row["last_name"]
    full_name = first + " " + last
    full_name_list.append(full_name)

print(full_name_list)

names_with_e = []

for name in full_name_list:
    if "e" in name.lower():
        names_with_e.append(name)

print(names_with_e)