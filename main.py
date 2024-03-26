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
    Locator(By.NAME, 'email', value='relig87936@storesr.com'),
    Locator(By.NAME, 'password', value='123456')
]
while globals.driver.current_url == url:
    elements = []
    for locator in locators:
        elements.append(locator.get())
        locator.set(elements[-1])
    elements[-1].send_keys(Keys.ENTER)

url = 'https://www.correoargentino.com.ar/MiCorreo/public/envio'
globals.driver.get(url)

#Delete previous tasks
envios_previos = Locator(By.XPATH, '//*[@id="divListado"]/div[1]').get()
if envios_previos.text != 'Sin envios cargados':
    locators = [
        Locator(By.XPATH, '//*[@id="divListado"]/div[1]/table/thead[1]/tr/td/div/label', button=True),
        Locator(By.XPATH, '//*[@id="page-wrapper"]/div[1]/div[5]/div/div[2]/button', button=True)
    ]
    elements = []
    for locator in locators:
        elements.append(locator.get())
        locator.set(elements[-1])
    btn_aceptar_locator = Locator(By.XPATH, '//*[@id="mensajeModalFooterGen"]/button[1]', button=True)
    btn_aceptar_locator.set(btn_aceptar_locator.get())
    
datos_sucursal = Locator(By.CLASS_NAME, 'datosSucursal').get()
btn_siguiente = Locator(By.ID, 'btn-siguiente-envios', button=True)
btn_siguiente.set(btn_siguiente.get())

locators = [
    Locator(By.NAME, 'destino_nombre', 'nombre'),
    Locator(By.NAME, 'destino_provincia', id='Provincia'),
    Locator(By.NAME, 'destino_localidad', id='Localidad'),
    Locator(By.NAME, 'destino_calle', id='Calle'),
    Locator(By.NAME, 'destino_altura', id='Altura'),
    Locator(By.NAME, 'destino_cp', id='Código postal'),
    Locator(By.NAME, 'destino_mail', 'mail@mail.com'),
    Locator(By.XPATH, "//*[@id='panel2']/div/div/div/div[4]/div/button[2]", button=True)
]

elements = []
for locator in locators:
    elements.append(locator.get())
    locator.set(elements[-1])

locators = [
    Locator(By.NAME, 'tipo_producto', key=Keys.ARROW_DOWN),
    Locator(By.NAME, 'peso', id='Peso(kg)'),
    Locator(By.NAME, 'largo', id='Largo(cm)'),
    Locator(By.NAME, 'ancho', id='Ancho(cm)'),
    Locator(By.NAME, 'altura', id='Altura(cm)'),
    Locator(By.NAME, 'valor', value='1'),
    Locator(By.ID, 'btnagregar', button=True)
]

elements = []
for locator in locators:
    elements.append(locator.get())
    locator.set(elements[-1])

locators = [
    Locator(By.XPATH, '//*[@id="divListado"]/div[1]/table/thead[1]/tr/td/div/label', button=True),
    Locator(By.ID, 'btnpedido', button=True)
]
elements = []
for locator in locators:
    elements.append(locator.get())
    locator.set(elements[-1])

precio = Locator(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div[1]/div/div[3]/span').get().text
print('El costo de envío es: ' + precio)