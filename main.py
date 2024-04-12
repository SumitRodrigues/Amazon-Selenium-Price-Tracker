from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

from notifypy import  Notify

notification = Notify()
notification.title = "Extracting Data"
notification.message = "Extracting data from Amazon"
notification.send()

options = Options()
# options.add_argument("--headless")
