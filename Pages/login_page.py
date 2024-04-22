from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

input_login_selector = (By.XPATH, '//*[@id="field-5"]')
input_password_selector = (By.XPATH, '//*[@id="field-6"]')
button_enter_selector = (By.XPATH, '//*[@class="envelope__footer"]//*[@class="bar__button button button--solid"]')
next_step_element_selector=(By.XPATH, '//*[@class="envelope__header"]//div[@class="caption"][text()="Личные данные"]')
error_data_selector = (By.XPATH, '//*[@id="jGrowl"]/div[2]/div[2]')
class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://arnypraht.com/login/')
    def input_login(self):
        return self.find(input_login_selector)

    def send_keys_in_login(self, word):
        return self.input_login().send_keys(word)

    def input_password(self):
        return self.find(input_password_selector)

    def send_keys_in_password(self, word):
        return self.input_password().send_keys(word)

    def button_enter(self):
        return self.find(button_enter_selector)

    def is_data_correct(self):
        return self.find(next_step_element_selector).is_enabled()

    def is_data_incorrect(self):
        return self.find(error_data_selector).is_enabled()