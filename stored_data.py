import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example-ecommerce.com/discounted-products"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract product details (assuming the structure of the page)
products = soup.find_all("div", class_="product")

for product in products:
    product_name = product.find("h2", class_="product-name").text.strip()
    price = float(product.find("span", class_="price").text.strip().replace("$", ""))
    discount_percent = int(product.find("span", class_="discount").text.strip().replace("%", ""))
    original_price = float(product.find("span", class_="original-price").text.strip().replace("$", ""))
    product_url = product.find("a", class_="product-link")["href"]
    
    # Insert the product data into the MySQL database
    insert_product_data(product_name, price, discount_percent, original_price, product_url) # type: ignore
