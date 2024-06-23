from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=10):
        """ allows to interact with the element which may be not visible"""
        return wait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        """ allows to interact with the element which may be not visible"""
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def go_to_element(self, el, timeout=10):
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
