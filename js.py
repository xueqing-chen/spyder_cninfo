from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)
htmlSource = driver.page_source