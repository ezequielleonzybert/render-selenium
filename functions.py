def WaitLocators(driver, By, wait, names_values, locators):
    for i, (name, value) in enumerate(names_values.items()):
        locators.append(driver.find_element(By.NAME, name))
        wait.until(lambda d : locators[i].is_displayed())

def FillLocators(names_values, locators):
    for i, (name, value) in enumerate(names_values.items()):
        locators[i].send_keys(value)

def InputValues(names_values):
    for (name, value) in names_values.items():
        if value == None:
            print(name + ': ')
            names_values[name] = input()