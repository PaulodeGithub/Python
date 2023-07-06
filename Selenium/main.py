from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to your ChromeDriver executable
chrome_driver_path = "C:\Development\chromedriver.exe"

# Set the ChromeDriver path and version
selenium_service = Service(chrome_driver_path, chrome_version=114)

# Create ChromeOptions and specify headless mode if desired
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

# Create the WebDriver instance
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)

# Open the desired URL
driver.get("https://en.wikipedia.org/wiki/Brazil")

# Find the <title> element and print its text
title_element = driver.find_element(By.XPATH, "//head/title")
print(title_element.get_attribute("textContent"))

# Quit the WebDriver 
# adding a test to git
driver.quit()


