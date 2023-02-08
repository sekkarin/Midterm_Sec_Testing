import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



s = Service('C:\driver\msedgedriver.exe')
driver = webdriver.Edge(service=s)

driver.get("https://nxtgenaiacademy.com/demo-site/")

driver.find_element(By.ID, "vfb-5").send_keys('Sekkarin')
driver.find_element(By.ID, "vfb-7").send_keys('Singhayoo')

driver.find_element(By.XPATH, "//label[contains(.,'Male')]")
driver.find_element(By.ID, "vfb-13-address").send_keys('11/1')
driver.find_element(By.ID, "vfb-13-address-2").send_keys('123')
driver.find_element(By.ID, "vfb-13-city").send_keys('kennnn')
driver.find_element(By.ID, "vfb-13-state").send_keys('nakornpathom')
driver.find_element(By.ID, "vfb-13-zip").send_keys('nakornpathom')
driver.find_element(By.XPATH, "//li[@id='item-vfb-13']/div/span[6]/span/span/span")
driver.find_element(By.ID, "vfb-14").send_keys('644259021@webmail.npru.ac.th')
driver.find_element(By.XPATH, "//li[@id='item-vfb-16']/span/span/span/span/span[2]")
driver.find_element(By.ID, "vfb-19").send_keys('08000000000')
driver.find_element(By.XPATH, "//li[@id='item-vfb-20']/div/span/label")
driver.find_element(By.ID, "vfb-23").send_keys('Hello wolrd')
driver.find_element(By.ID, "vfb-3").send_keys('55')
driver.find_element(By.ID, "vfb-4").click()
assert "Registration Form is Successfully Submitted." in driver.page_source

time.sleep(10)
driver.close()
