import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

website = "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm"
path= 'D:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

duration = driver.find_element_by_xpath('//option[@value="week"]')
duration.click()

stock = driver.find_element_by_xpath('//input[@name="symbol"]')
stock.click()
stock.send_keys('VEDANTA')
stock.send_keys(Keys.RETURN)


getdata_button = driver.find_element_by_xpath('//input[@type="button"]')
getdata_button.click()

time.sleep(5)

driver.quit()