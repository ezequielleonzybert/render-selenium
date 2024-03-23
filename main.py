import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.system("cls")

email = "choboku@gmail.com"
password = "choboku"

def fill_form():
    btn_siguiente = driver.find_element(By.ID, "btn-siguiente-envios")
    btn_siguiente.click()
    time.sleep(1)

    destino_nombre = driver.find_element(By.NAME, "destino_nombre")
    destino_nombre.send_keys("pepe")
    destino_provincia = driver.find_element(By.NAME, "destino_provincia")
    destino_provincia.send_keys("B")
    destino_localidad  = driver.find_element(By.NAME, "destino_localidad")
    destino_localidad.send_keys("moron")
    destino_calle = driver.find_element(By.NAME, "destino_calle")
    destino_calle.send_keys("ramona")
    destino_altura = driver.find_element(By.NAME, "destino_altura")
    destino_altura.send_keys("123")
    destino_cp = driver.find_element(By.NAME, "destino_cp")
    destino_cp.send_keys("1825")
    destino_mail = driver.find_element(By.NAME, "destino_mail")
    destino_mail.send_keys("pepe@pepe.com")

    btn_siguiente2 = driver.find_element(By.XPATH, """//*[@id="panel2"]/div/div/div/div[4]/div/button[2]""")
    btn_siguiente2.click()
    
    time.sleep(1)

    tipo_producto = driver.find_element(By.NAME, "tipo_producto")
    tipo_producto.send_keys(Keys.ARROW_DOWN)
    peso = driver.find_element(By.NAME, "peso")
    peso.send_keys("1")
    largo = driver.find_element(By.NAME, "largo")
    largo.send_keys("1")
    ancho = driver.find_element(By.NAME, "ancho")
    ancho.send_keys("1")
    altura = driver.find_element(By.NAME, "altura")
    altura.send_keys("1")
    valor = driver.find_element(By.NAME, "valor")
    valor.send_keys("1")

service = Service(executable_path="chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.correoargentino.com.ar/MiCorreo/public/login")

input_email = driver.find_element(By.ID,"email")
input_password = driver.find_element(By.ID,"password")
input_email.send_keys(email)
input_password.send_keys(password + Keys.ENTER)
if driver.current_url == "https://www.correoargentino.com.ar/MiCorreo/public/login":
    input_email = driver.find_element(By.ID,"email")
    input_password = driver.find_element(By.ID,"password")
    input_email.send_keys(email)
    input_password.send_keys(password + Keys.ENTER)

driver.get("https://www.correoargentino.com.ar/MiCorreo/public/envio")

fill_form()

btn_agregar = driver.find_element(By.ID, "btnagregar")
btn_agregar.click()

driver.get("https://www.correoargentino.com.ar/MiCorreo/public/logout")
driver.close()
