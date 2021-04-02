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

login = driver.find_element_by_class_name("name")
login.click()

try:
	registrar = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"btnRegistrar")))
	registrar.click()
	
	nombre = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.NAME,"nombre")))
	nombre.send_keys("juanito")
	
	apellido = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.NAME,"apellido")))
	apellido.send_keys("perez")
	
	Dia = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"day")))
	Dia.send_keys("10")

	Mes = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"month")))
	Mes.send_keys("05")

	Ano = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"year")))
	Ano.send_keys("1995")

	telefono = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.NAME,"tlf")))
	telefono.send_keys("942946393")
	
	email = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.NAME,"email")))
	email.send_keys("david.cripto@hotmail.com")

	clave = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.NAME,"password")))
	clave.send_keys("David123*")
	
	claveafirmativa = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.NAME,"repeat_password")))
	claveafirmativa.send_keys("David123*")

	registrarme = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.ID,"registrarme")))
	registrarme.click()

except:
	time.sleep(60)
	driver.close()
