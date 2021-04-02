from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui


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
	
	login = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"submit-login")))
	login.click()

	pyautogui.moveTo(780, 150, duration=2, tween=pyautogui.easeInOutQuad)
	pyautogui.click()

	pyautogui.moveTo(500, 250, duration=2, tween=pyautogui.easeInOutQuad)
	pyautogui.click()

	new_password = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"new_password")))
	new_password.send_keys("david123@")

	confirm_new_password = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"confirm_new_password")))
	confirm_new_password.send_keys("david123@")


	pyautogui.keyDown('Enter')
except:
	time.sleep(20)