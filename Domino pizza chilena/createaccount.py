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

login = driver.find_element_by_id("iniciaSesion")
login.click()

try:
	create = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.LINK_TEXT,"CREA UNO")))
	create.click()
	
	nombre = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"name")))
	nombre.send_keys("juanito")
	
	apellido = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"surname")))
	apellido.send_keys("perez")
	
	email = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"email")))
	email.send_keys("david.cripto@hotmail.com")
	
	telefono = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"phone")))
	telefono.send_keys("12345678")
	
	clave = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"pass")))
	clave.send_keys("david12")
	
	claveafirmativa = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"passConfirmation")))
	claveafirmativa.send_keys("david12")
	
	pyautogui.keyDown('Enter')

	
except:
	time.sleep(60)
	driver.close()
