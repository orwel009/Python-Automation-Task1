from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\SoftwareTesting\AutomatedPrograms\chromedriver.exe")

try:
    driver.get("https://www.flipkart.com/")
    time.sleep(2)
    print("Testcase 1:")
    searchBar = driver.find_element(By.NAME,"q")
    searchBar.send_keys("macbook air m2")
    time.sleep(1)
    searchBar.send_keys(Keys.ENTER)
    time.sleep(3)
    if driver.title == "Macbook Air M2- Buy Products Online at Best Price in India - All Categories | Flipkart.com":
        print("Pass")
    else:
        print("Fail")
finally:
    driver.quit()