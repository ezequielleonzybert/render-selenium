import globals
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locator import Locator

url = 'https://www.correoargentino.com.ar/MiCorreo/public/login'
globals.driver.get(url)

locators = [
    Locator(By.NAME, 'email', 'relig87936@storesr.com'),
    Locator(By.NAME, 'password', '123456')
]
while globals.driver.current_url == url:
    elements = []
    for locator in locators:
        elements.append(locator.get())
        locator.fill(elements[-1])
    elements[-1].send_keys(Keys.ENTER)

url = 'https://www.correoargentino.com.ar/MiCorreo/public/envio'
globals.driver.get(url)

#Delete previous tasks
envios_previos = Locator(By.XPATH, '//*[@id="divListado"]/div[1]').get()
if envios_previos.text != 'Sin envios cargados':
    #Here the code
    pass 

datos_sucursal = Locator(By.CLASS_NAME, 'datosSucursal').get()
btn_siguiente = Locator(By.ID, 'btn-siguiente-envios').get()
btn_siguiente.click()

locators = [
    Locator(By.NAME, 'destino_nombre', 'nombre'),
    Locator(By.NAME, 'destino_provincia', id='Provincia'),
    Locator(By.NAME, 'destino_localidad', id='Localidad'),
    Locator(By.NAME, 'destino_calle', id='Calle'),
    Locator(By.NAME, 'destino_altura', id='Altura'),
    Locator(By.NAME, 'destino_cp', id='Código postal'),
    Locator(By.NAME, 'destino_mail', 'mail@mail.com')
]

elements = []
for locator in locators:
    elements.append(locator.get())
    locator.fill(elements[-1])

btn_siguiente = Locator(By.XPATH, "//*[@id='panel2']/div/div/div/div[4]/div/button[2]").get()
btn_siguiente.click()


input()