from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

from notifypy import  Notify

notification = Notify()
notification.title = "Extracting Data"
notification.message = "Extracting data from Amazon"
notification.send()

options = Options()
# options.add_argument("--headless")
# options.add_argument("--proxy-server=gate.nodemaven.com:8080")

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

with open("products.txt") as f:
    products = f.readlines()


driver = webdriver.Chrome(options=options)

i = 0
for product in products:
    driver.get(product)
    i += 1
    page_source = driver.page_source
    with open(f"data/{i}.html", "w", encoding="utf-8") as f:
        f.write(page_source)