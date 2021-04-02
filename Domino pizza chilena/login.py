from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time


PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://dominospizza.cl")
print(driver.title)

login = driver.find_element_by_id("iniciaSesion")
login.click()

try:
	user = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"user_email")))
	user.send_keys("david.cripto@hotmail.com")

	password = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"user_password")))
	password.send_keys("david123@")
	pyautogui.keyDown("Enter")

except:
	time.sleep(20)
	driver.close()

