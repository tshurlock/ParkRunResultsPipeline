
#wrap this as a function to run from main

import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#Placeholder runner number, will be added in main when
runner = str(input("Enter ParkRun number"))
# Constants
ParkrunURL = "https://www.parkrun.org.uk//parkrunner//" + runner + "//all//"

# Set up Chrome driver (path to chromedriver)
driver_service = Service("C:\\Users\\Tim\\Desktop\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

#Open Canvas login page
driver.get(ParkrunURL)

# Find the table element using Selenium
table = driver.find_element(By.XPATH, "(//table)[3]")
#table = driver.find_element(By.ID, "results")

print(table)

# Parse the table HTML using BeautifulSoup
soup = BeautifulSoup(table.get_attribute("outerHTML"), "html.parser")

# Convert the table to a pandas dataframe
df = pd.read_html(str(soup))[0]

print(df)
df.to_csv("C:\\Users\\Tim\\Desktop\\prResults.csv", index=True)