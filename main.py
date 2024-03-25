import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import WaitLocators, FillLocators, InputValues

service = Service(executable_path='chromedriver.exe')
chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, timeout=10)
url = 'https://www.correoargentino.com.ar/MiCorreo/public/login'
driver.get(url)

email = 'choboku@gmail.com'
# print('password: ')
password = 'choboku'
names_values = {'email':email, 'password':password}

while driver.current_url == url:
    locators = []
    WaitLocators(driver, By, wait, names_values, locators)
    FillLocators(names_values, locators)
    locators[-1].send_keys(Keys.ENTER)

url = 'https://www.correoargentino.com.ar/MiCorreo/public/envio' 
driver.get(url)
datos_sucursal = driver.find_element(By.CLASS_NAME, 'datosSucursal')
wait.until(lambda d : datos_sucursal.is_displayed())
btn_siguiente = driver.find_element(By.ID, 'btn-siguiente-envios')
btn_siguiente.click()

names_values = {
    'destino_nombre': 'nombre',
    'destino_provincia': None,
    'destino_localidad': None,
    'destino_calle': None,
    'destino_altura': None,
    'destino_cp': None,
    'destino_mail': 'mail@mail.com'
    }
locators = []
WaitLocators(driver, By, wait, names_values, locators)
InputValues(names_values)
FillLocators(names_values, locators)
btn_siguiente = driver.find_element(By.XPATH, "//*[@id='panel2']/div/div/div/div[4]/div/button[2]")
wait.until(lambda d : btn_siguiente.is_displayed())
btn_siguiente.click()

tipo_producto = driver.find_element(By.NAME, 'tipo_producto')
wait.until(lambda d : tipo_producto.is_displayed())
tipo_producto.send_keys(Keys.ARROW_DOWN)

names_values = {
    'peso': None,
    'largo': None,
    'ancho': None,
    'altura': None,
    'valor': '1',
    }
locators = []
WaitLocators(driver, By, wait, names_values, locators)
InputValues(names_values)
FillLocators(names_values, locators)
btn_agregar = driver.find_element(By.ID, 'btnagregar')
wait.until(lambda d : btn_agregar.is_displayed())
btn_agregar.click()

checkbox = driver.find_element(By.XPATH, '//*[@id="divListado"]/div[1]/table/thead[1]/tr/td/div/label')
wait.until(lambda d : checkbox.is_displayed())
checkbox.click()

btn_pedido = driver.find_element(By.ID, 'btnpedido')
wait.until(lambda d : btn_pedido.is_displayed())
btn_pedido.click()

input()
driver.get('https://www.correoargentino.com.ar/MiCorreo/public/logout')
driver.close()
