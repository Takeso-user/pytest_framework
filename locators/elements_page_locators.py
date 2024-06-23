from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "*[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "*[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "*[id='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "*[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckboxLocators:
    EXPAND_ALL = (By.XPATH, '//*[@id="tree-node"]/div/button[1]')
    CHECKBOX_HOME = (By.CSS_SELECTOR, '#tree-node > ol > li > span > label > span.rct-checkbox')
    RESULT = (By.CSS_SELECTOR, '#result')
    RESULT_LIST = (By.CSS_SELECTOR, '#result .text-success')
