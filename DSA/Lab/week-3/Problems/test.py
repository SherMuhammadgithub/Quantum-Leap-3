import sys
import threading
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar

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

# Global variables for control
is_paused = False
is_stopped = False
total_products_to_scrape = 500
total_products_scraped = 0

# Define lists to store data
product_names = []
product_prices = []
product_links = []
product_ratings = []
product_images = []

# Function to scrape products from the page
def scrape_products():
    global total_products_scraped, is_paused, is_stopped

    while total_products_scraped < total_products_to_scrape and not is_stopped:
        if is_paused:
            print("Scraping paused...")
            time.sleep(1)  # Wait while paused
            continue

        # Get the page content and scrape products
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        products = soup.find_all('a', class_='pc-custom-link')

        # Handle case where no products are found
        if not products:
            print("No products found on the page.")
            break

        for product in products:
            try:
                # Get product name
                name = product.find('div', class_='card-jfy-title').text.strip()
                product_names.append(name)

                # Get product price
                price = product.find('span', class_='price').text.strip()
                product_prices.append(price)

                # Get product link
                link = product['href']
                product_links.append(f"https://www.daraz.pk{link}")

                # Get product rating (if available)
                rating = product.find('div', class_='card-jfy-rating-layer').get('style')
                rating_percentage = rating.split(':')[1].replace('%', '').strip()
                product_ratings.append(rating_percentage)

                # Get product image URL
                image = product.find('img')['src']
                product_images.append(image)

            except Exception as e:
                print(f"Error processing product: {e}")

        total_products_scraped += len(products)
        print(f"Total products scraped: {total_products_scraped}")

        # Update progress in the UI
        window.update_progress(total_products_scraped)

        if is_stopped:
            print("Scraping stopped.")
            break

        # Scroll down and click "Load More" button
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'load-more-button'))
            )
            load_more_button.click()
            time.sleep(5)  # Wait for more products to load
        except Exception as e:
            print("No 'Load More' button found or unable to click:", e)
            break  # Exit loop if there are no more products to load

# Control functions for pausing, resuming, and stopping scraping
def pause_scraping():
    global is_paused
    is_paused = True
    print("Scraping paused.")

def resume_scraping():
    global is_paused
    is_paused = False
    print("Scraping resumed.")

def stop_scraping():
    global is_stopped
    is_stopped = True
    print("Scraping stopped.")
    
# Save scraped data to CSV
def save_data_to_csv():
    df = pd.DataFrame({
        'Product Name': product_names,
        'Price': product_prices,
        'Product Link': product_links,
        'Rating (%)': product_ratings,
        'Image URL': product_images
    })
    df.to_csv('daraz_products.csv', index=False)
    print("Data saved to daraz_products.csv")

# PyQt5 UI class
class ScraperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Daraz Scraper Control')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        # Create a progress label and bar
        self.progress_label = QLabel('Progress: 0/500')
        self.layout.addWidget(self.progress_label)
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(total_products_to_scrape)
        self.layout.addWidget(self.progress_bar)

        # Buttons
        self.start_button = QPushButton('Start Scraping')
        self.start_button.clicked.connect(self.start_scraping)
        self.layout.addWidget(self.start_button)
        
        self.pause_button = QPushButton('Pause Scraping')
        self.pause_button.clicked.connect(self.pause_scraping)
        self.layout.addWidget(self.pause_button)

        self.resume_button = QPushButton('Resume Scraping')
        self.resume_button.clicked.connect(self.resume_scraping)
        self.layout.addWidget(self.resume_button)
        
        self.stop_button = QPushButton('Stop Scraping')
        self.stop_button.clicked.connect(self.stop_scraping)
        self.layout.addWidget(self.stop_button)
        
        self.setLayout(self.layout)
    
    def start_scraping(self):
        threading.Thread(target=scrape_products, daemon=True).start()
    
    def pause_scraping(self):
        pause_scraping()

    def resume_scraping(self):
        resume_scraping()

    def stop_scraping(self):
        stop_scraping()

    # Function to update progress from the scraping loop
    def update_progress(self, value):
        self.progress_label.setText(f'Progress: {value}/500')
        self.progress_bar.setValue(value)

# Main execution
app = QApplication(sys.argv)
window = ScraperApp()
window.show()
sys.exit(app.exec_())
