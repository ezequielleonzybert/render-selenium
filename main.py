import globals
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator
from flask import Flask, request

app = Flask(__name__)

@app.route('/consulta', methods=['POST'])
def consulta():
    return {
        'destino_provincia': request.form['destino_provincia'],
        'destino_localidad': request.form['destino_localidad'],
        'destno_calle': request.form['destno_calle'],
        'destino_altura': request.form['destino_altura'],
        'destino_cp': request.form['destino_cp'],
        'peso': request.form['peso'],
        'largo': request.form['largo'],
        'ancho': request.form['ancho'],
        'altura': request.form['altura']
    }

consulta = consulta()

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
        Locator(By.CSS_SELECTOR, '#divListado > div.table-responsive.dvEnvios > table > thead.origen > tr > td > div > label', button=True),
        Locator(By.CSS_SELECTOR, '#page-wrapper > div.envio > div:nth-child(5) > div > div:nth-child(3) > button', button=True)
    ]
    elements = []
    for locator in locators:
        elements.append(locator.get())
        locator.set(elements[-1])
    btn_aceptar_locator = Locator(By.CSS_SELECTOR, '#mensajeModalFooterGen > button:nth-child(1)', button=True)
    btn_aceptar_locator.set(btn_aceptar_locator.get())
    
datos_sucursal = Locator(By.CLASS_NAME, 'datosSucursal').get()
btn_siguiente = Locator(By.CSS_SELECTOR, '#btn-siguiente-envios', button=True)
btn_siguiente.set(btn_siguiente.get())

locators = [
    Locator(By.NAME, 'destino_nombre', value='nombre'),
    Locator(By.NAME, 'destino_provincia', value=consulta.destino_provincia, id='Provincia'),
    Locator(By.NAME, 'destino_localidad', value=consulta.destino_localidad, id='Localidad'),
    Locator(By.NAME, 'destino_calle', value=consulta.destio_calle,  id='Calle'),
    Locator(By.NAME, 'destino_altura', value=consulta.destino_altura, id='Altura'),
    Locator(By.NAME, 'destino_cp', value=consulta.destino_cp, id='Código postal'),
    Locator(By.NAME, 'destino_mail', value='mail@mail.com'),
    Locator(By.CSS_SELECTOR, "#panel2 > div > div > div > div.form-group > div > button.btn.btn-primary.boton-siguiente.btn-siguiente-envios.ayudita", button=True)
]

print('\nDatos del destino:')
elements = []
for locator in locators:
    elements.append(locator.get())
    locator.set(elements[-1])

locators = [
    Locator(By.NAME, 'tipo_producto', key=Keys.ARROW_DOWN),
    Locator(By.NAME, 'peso', value=consulta.peso, id='Peso(kg)'),
    Locator(By.NAME, 'largo', value=consulta.largo, id='Largo(cm)'),
    Locator(By.NAME, 'ancho', value=consulta.ancho, id='Ancho(cm)'),
    Locator(By.NAME, 'altura', value=consulta.altura, id='Altura(cm)'),
    Locator(By.NAME, 'valor', value='1'),
    Locator(By.CSS_SELECTOR, '#btnagregar', button=True)
]

elements = []
for locator in locators:
    elements.append(locator.get())
    locator.set(elements[-1])

locators = [
    Locator(By.CSS_SELECTOR, '#divListado > div.table-responsive.dvEnvios > table > thead.origen > tr > td > div > label', button=True),
    Locator(By.CSS_SELECTOR, '#btnpedido', button=True)
]

elements = []
for locator in locators:
    elements.append(locator.get())
    locator.set(elements[-1])

precio = Locator(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div[1]/div/div[3]/span').get().text
print('El costo de envío es: ' + precio[:-3])

url = 'https://www.correoargentino.com.ar/MiCorreo/public/logout'
globals.driver.get(url)
globals.driver.close()