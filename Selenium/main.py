
from selenium import webdriver

chrome_driver_path ="C:\Development\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/ano-morte-Ayrton-Senna-Portuguese/dp/1548656461/ref=sr_1_4?keywords=books+ayrton+senna&qid=1688569006&refinements=p_n_feature_nine_browse-bin%3A3291445011&rnid=3291435011&s=books&sr=1-4")

driver.find_element(by="a-page")




# driver.close()
driver.quit()