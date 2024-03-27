from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import platform

OS = platform.system()
if OS == 'Windows':
    service = Service(executable_path='chromedriver.exe')
elif OS == 'Linux':
    service = Service(executable_path='/chromedriverlinux')
options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)