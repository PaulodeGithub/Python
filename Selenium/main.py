from selenium import webdriver
chrome_driver_path = "C:\Development\chromedriver_win32"

driver = webdriver.Chrome(options=chrome_driver_path)

driver.get("https://www.amazon.co.uk/books-used-books-textbooks/b?ie=UTF8&node=266239")