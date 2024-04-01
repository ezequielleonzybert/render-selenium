import globals
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locator:
    def __init__(self, type, path, value=None, key=None, button=False, id=None):
        self.type = type
        self.path = path
        self.value = value   
        self.key = key     
        self.button = button
        self.id = id

    def get(self):
        locator = (self.type, self.path)
        element = globals.wait.until(EC.visibility_of_element_located(locator))
        return element

    def set(self, element):
        if self.value:
            element.send_keys(self.value)
        else: 
            if self.key:
                element.send_keys(self.key)
            elif self.button:
                globals.driver.execute_script(
                    f"document.querySelector('{self.path}').click()"
                )
                # element.click()
            else:
                print(self.id + ': ')
                self.value = input()
                element.send_keys(self.value)


    

    
