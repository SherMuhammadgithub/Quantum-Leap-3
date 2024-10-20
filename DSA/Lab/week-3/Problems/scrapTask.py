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

# Set Chrome options (if needed)
chrome_options = webdriver.ChromeOptions()

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver with the Service object and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Daraz website
driver.get('https://www.daraz.pk/#hp-just-for-you')

# Wait until the product cards are present on the page
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'pc-custom-link'))
)

# Define lists to store data
product_names = []
product_prices = []
product_links = []
product_ratings = []
product_images = []

# Total number of products to scrape
total_products_to_scrape = 25000
total_products_scraped = 0

# Function to scrape products from the page
def scrape_products():
    global total_products_scraped
    # Get the page content
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    # Find product elements and extract data
    products = soup.find_all('a', class_='pc-custom-link')  # Adjust this if necessary
    
    # Loop over each product and extract relevant data
    for product in products:
        # Get product name
        try:
            name = product.find('div', class_='card-jfy-title').text.strip()
            product_names.append(name)
        except:
            product_names.append("N/A")
        
        # Get product price
        try:
            price = product.find('span', class_='price').text.strip()
            product_prices.append(price)
        except:
            product_prices.append("N/A")

        # Get product link
        try:
            link = product['href']
            product_links.append(f"https://www.daraz.pk{link}")
        except:
            product_links.append("N/A")

        # Get product rating (if available)
        try:
            rating = product.find('div', class_='card-jfy-rating-layer').get('style')
            rating_percentage = rating.split(':')[1].replace('%', '').strip()
            product_ratings.append(rating_percentage)
        except:
            product_ratings.append("N/A")

        # Get product image URL
        try:
            image = product.find('img')['src']
            product_images.append(image)
        except:
            product_images.append("N/A")

    total_products_scraped += len(products)
    print(f"Total products scraped: {total_products_scraped}")

# Main scraping loop, continue until 25,000 products are gathered
while total_products_scraped < total_products_to_scrape:
    # Scrape the current batch of products
    scrape_products()

    # Scroll down and try to click the "Load More" button if it exists
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'load-more-button'))
        )
        load_more_button.click()
        time.sleep(5)  # Wait for more products to load
    except Exception as e:
        print("No 'Load More' button found or unable to click:", e)
        break  # Exit loop if there are no more products to load

# Create a DataFrame to store the product data
df = pd.DataFrame({
    'Product Name': product_names,
    'Price': product_prices,
    'Product Link': product_links,
    'Rating (%)': product_ratings,
    'Image URL': product_images
})

# Save the data to a CSV file
df.to_csv('daraz_products.csv', index=False)

# Close the browser
driver.quit()

print("Scraping completed and data saved to 'daraz_products.csv'")
