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
driver.get("https://www.italki.com/?gclid=CjwKCAjw2K6lBhBXEiwA5RjtCVtyTCyZKJlR3263ZJyO-rpJenhPqanLNO-v3hpaLGRNOuVjzho5fhoC-N0QAvD_BwE&utm_campaign=pmax_rmt_en_nofpnopinterest_ESW_UK&utm_content=bau_2022&utm_medium=pmax&utm_source=google_ads&utm_term=")

# Find the <title> element and print its text
title_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/footer/div[4]/div/div[2]/div[2]/a[7]')
print(title_element.get_attribute("style"))

# Quit the WebDriver 
# adding a test to git
driver.quit()


