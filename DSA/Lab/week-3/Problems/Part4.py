from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set the path to the ChromeDriver executable
chrome_driver_path = 'C:/Users/Sher/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe'

# Set Chrome options to ignore SSL errors (optional, if needed)
chrome_options = webdriver.ChromeOptions()

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver with the Service object and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get('http://eduko.spikotech.com')

# Wait until the course data is present on the page 
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'card'))
)

# Get the page content after ensuring it has loaded
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

# Define lists to store data
course_titles = []
course_descriptions = []
course_instrctors = []
course_links = []
semesters = []
course_codes = []

# Find course elements and extract data
courses = soup.find_all('div', class_='card')

for course in courses:
    # Get course title
    title = course.find('h4', class_='card-title').text.strip()
    course_titles.append(title)
    
    # Get instructor name
    instructor = course.find_all('h7')[0].text.strip()
    course_instrctors.append(instructor)
    
    # Get semester information
    semester = course.find_all('h7')[1].text.strip()
    semesters.append(semester)
    
    # Get course description
    description = course.find('p', class_='card-text').text.strip()
    course_descriptions.append(description)
    
    # Get the link to the course details page
    course_link = course.find('a', href=True)['href']
    course_links.append(f"http://eduko.spikotech.com{course_link}")

    # Open the course link
    driver.get(f"http://eduko.spikotech.com{course_link}")

    # Wait untill the course code element is present on the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'CourseCode'))
    )
    
    # Checking if the Loading... is still present
    try:
       loading_text =  WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="CourseCode" and text()="Loading..."]'))
        )
       if loading_text:
        # If loading text is present, wait  
          WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, '//*[@id="CourseCode" and text()="Loading..."]'))
          )     
    except:
        pass

    # Get the course code
    course_code_element = driver.find_element(By.ID, 'CourseCode')
    course_code = course_code_element.text.strip()
    course_codes.append(course_code)

    # Go back to the main page
    driver.back()
    time.sleep(1)


# Create a DataFrame
df = pd.DataFrame({
    'Title': course_titles,
    'Instructor': course_instrctors,
    'Semester': semesters,
    'Description': course_descriptions,
    'Link': course_links,
    'Code': course_codes
})

# Save to CSV
df.to_csv('courses.csv', index=False)

# Close the browser
driver.quit()








# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import csv

# # Set up the WebDriver (you can change this to Firefox or another browser if needed)
# driver = webdriver.Chrome(executable_path='C:/Users/Sher/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe')

# # Open the Daraz page
# driver.get('https://www.daraz.pk/#hp-just-for-you')

# # Scroll down to load the page properly
# time.sleep(5)

# # Function to scrape product data
# def get_product_data():
#     products = driver.find_elements(By.CSS_SELECTOR, '.c2prKC')
#     product_list = []
#     for product in products:
#         try:
#             product_name = product.find_element(By.CSS_SELECTOR, '.c16H9d a').text
#             product_price = product.find_element(By.CSS_SELECTOR, '.c3gUW0').text
#             product_link = product.find_element(By.CSS_SELECTOR, '.c16H9d a').get_attribute('href')
#             product_list.append([product_name, product_price, product_link])
#         except Exception as e:
#             print(f"Error extracting product: {e}")
#     return product_list

# # Function to save data to CSV
# def save_to_csv(data, filename='daraz_products.csv'):
#     with open(filename, 'a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)

# # Scrape until we reach 25,000 products
# total_products = 0
# max_products = 25000

# while total_products < max_products:
#     # Get product data
#     products = get_product_data()
#     total_products += len(products)
#     print(f"Fetched {len(products)} products, Total: {total_products}")
    
#     # Save to CSV
#     save_to_csv(products)
    
#     # Scroll down and click "Load More" if it's available
#     try:
#         load_more_btn = driver.find_element(By.CSS_SELECTOR, '.ant-btn')
#         load_more_btn.click()
#         time.sleep(5)  # Wait for products to load
#     except Exception as e:
#         print("No 'Load More' button found, or error clicking:", e)
#         break

# # Close the browser after scraping
# driver.quit()
