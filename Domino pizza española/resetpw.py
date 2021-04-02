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

driver.get("https://dominospizza.es")
print(driver.title)

login = driver.find_element_by_class_name("name")
login.click()

try:	
	resetpw= WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.LINK_TEXT,("¿Olvidaste tus datos?"))))
	resetpw.click()
	
	email = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"email")))
	email.send_keys("david.cripto@hotmail.com")

	pyautogui.keyDown("Enter")


except:
	time.sleep(60)
	driver.quit()


