import globals
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locator:
    def __init__(self, type, path, value=None, id=None):
        self.type = type
        self.path = path
        self.value = value        
        self.id = id

    def get(self):
        locator = (self.type, self.path)
        element = globals.wait.until(EC.visibility_of_element_located(locator))
        return element

    def fill(self, element):
        if self.value:
            element.send_keys(self.value)
        else:
            print(self.id + ': ')
            self.value = input()
            element.send_keys(self.value)


    

    
