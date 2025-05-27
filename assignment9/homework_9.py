# get_books.py

import pandas as pd
import json
import time
import os

#Copy and paste from given code
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




#Task 3 #############################

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)


time.sleep(3)

items = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
#print(items)
#print(f"Found {len(items)} result items.")

results = []

for element in items: 
    #try: # Check to find title. If title can be find, make it a strip
    try:
        #print(element.get_attribute('innerHTML'))  # Debug: inspect what's inside
        title_ = element.find_element(By.CSS_SELECTOR, "h2.cp-title a span.title-content")
        title = title_.text.strip()
    except Exception as e:
        print("Title error:", e)
        title = "N/A"
    
    #Next will be trying to find author

    try:
        author_ = element.find_elements(By.CSS_SELECTOR, "a.author-link")
        author_name = []

        for a in author_:
            name = a.text.strip()      #get the text and remove any leading spaces
            author_name.append(name)   

        if author_name:
            authors = "; ".join(author_name)  
        else:
            authors = "N/A"
    except Exception as e:
        print("Author error:", e)
        authors = "N/A"

    
    try:
        format_elem = element.find_element(By.CSS_SELECTOR, "span.display-info-primary")
        format_with_year = format_elem.text.strip()
    except Exception as e:
        print("Format-Year error:", e)
        format_with_year = "N/A"

    book_data = {
        "Title": title,
        "Author": authors,
        "Format-Year": format_with_year
    }
    results.append(book_data)

df = pd.DataFrame(results)
df.to_csv("books.csv", index=False)
df.to_json("books.json", orient="records", indent=2)

driver.quit()

#Task 4

df.to_csv('get_books.csv', index=False)

# While the code above alrady does it, but here it is! Just do another one!... 
# Get_books and books is the exact same thing
# save the results list to get_books.json
with open('get_books.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Files saved successfully in assignment9 directory.")