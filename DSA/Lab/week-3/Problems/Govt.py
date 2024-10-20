
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time

start_time = time.time()
service = Service(
    executable_path="C:/Users/Sher/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Initialize lists to store data
titles = []
descriptions = []

# Set the number of pages to scrape
page_limit = 100  # Adjust as needed

# Loop through pages
for page in range(1, page_limit + 1):
    # Open the website
    driver.get(f"https://catalog.data.gov/dataset?q=&page={page}")
    time.sleep(3)  # Wait for the page to load

    # Get page content
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # Find the required data
    datasets = soup.find_all('div', class_='dataset-content')

    for dataset in datasets:
        title = dataset.find('h3').text.strip()
        description = dataset.find('p').text.strip()
        
        titles.append(title)
        descriptions.append(description)

# Prepare data for DataFrame
df = pd.DataFrame({"Title": titles, "Description": descriptions})
df.to_csv("datasets.csv", index=False, encoding="utf-8")

# Close the browser
driver.quit()

print('Data saved to datasets.csv')
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")