from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()


driver.get("https://owasp.org/www-project-top-ten/") # Get llin
time.sleep(3)  

# The path to go to the link
xpath = "//h2[@id='top-10-web-application-security-risks']/following-sibling::ul[1]/li"

items = driver.find_elements(By.XPATH, xpath)


vul = []
for li in items:
    try:
        a_tag = li.find_element(By.TAG_NAME, "a") #Finding the A which is where the elements and link to collect from
        title = a_tag.text.strip()
        link = a_tag.get_attribute("href")  # Taking the title and ading the href for link
        vul.append({"title": title, "link": link})
    except:
        continue  # skip if <a> tag not found


print("List of All links:", vul)

with open("owasp_top_10.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(vul)

driver.quit()
