from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium WebDriver (download ChromeDriver and specify its path)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the e-commerce website (Jumia for this example)
driver.get("https://www.jumia.com.ng/")

# Wait for the page to load
driver.implicitly_wait(10)

# Use BeautifulSoup to parse the page content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Example: Extract product names and prices
products = []
for item in soup.find_all('div', class_='info'):
    name = item.find('h3', class_='name').text.strip()
    price = item.find('div', class_='prc').text.strip()
    discount = item.find('div', class_='bdg _dsct').text.strip() if item.find('div', class_='bdg _dsct') else "0%"

    products.append({
        'name': name,
        'price': price,
        'discount': discount
    })

# Close the Selenium driver
driver.quit()

# Convert the list of products into a Pandas DataFrame
df = pd.DataFrame(products)

# Save to a CSV file or store it directly in a database (next step)
df.to_csv('discounted_products.csv', index=False)
