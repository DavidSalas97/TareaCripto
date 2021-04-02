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

driver.get("https://dominospizza.es")
print(driver.title)

login = driver.find_element_by_class_name("name")
login.click()

try:
	user = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"txtUser")))
	user.send_keys("david.cripto@hotmail.com")

	password = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"txtPass")))
	password.send_keys("¨David123*")

	login = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"btnLoginMenu")))
	login.click()

	editarperfil = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"editarPerfil")))
	editarperfil.click()

	editardatos = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"editarDatos")))
	editardatos.click()

	password = WebDriverWait(driver,20).until(
		EC.presence_of_element_located((By.ID,"_password")))
	password.send_keys("David123*")

	password = WebDriverWait(driver,20).until(
		EC.presence_of_element_located((By.ID,"_repeat_password")))
	password.send_keys("David123*")

	pyautogui.keyDown('Enter')
except:
	time.sleep(20)
	driver.quit()