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
	pyautogui.moveTo(600, 530, duration=2, tween=pyautogui.easeInOutQuad)
	pyautogui.click()
	
	email = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"email_reset_password")))
	email.send_keys("criptoesgrande1@hotmail.com")

	create = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"submit-reset-password")))
	create.click()


except:
	time.sleep(60)
	driver.quit()


