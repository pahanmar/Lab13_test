from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

input_login_selector = (By.XPATH, '//*[@id="office-auth-register-email"]')
input_password_selector = (By.XPATH, '//*[@id="office-register-form-password"]')
input_number_selector = (By.XPATH, '//*[@id="office-auth-register-mobilephone"]')
button_enter_selector = (By.XPATH, '//*[@class="envelope__footer"]//*[@type="submit"]')

male_gender_selector = (By.XPATH, '//*[@class="svg-symbol svg-symbol--male choice__variant-icon"]')
female_gender_selector = (By.XPATH, '//*[@class="svg-symbol svg-symbol--female choice__variant-icon"]')

date_day_selector = (By.XPATH, '//*[@class="select2-selection__placeholder"][text()="День"]')
date_month_selector = (By.XPATH, '//*[@class="select2-selection__placeholder"][text()="Месяц"]')
date_year_selector = (By.XPATH, '//*[@class="select2-selection__placeholder"][text()="Год"]')

date_day_input_selector = (By.XPATH, '//*[@class="select2-results__options"]//*[text()="03"]')
date_month_input_selector = (By.XPATH, '//*[@class="select2-results__options"]//*[text()="Апр"]')
date_year_input_selector = (By.XPATH, '//*[@class="select2-results__options"]//*[text()="2000"]')

checkbox_selector = (By.XPATH, '//*[@class="checkbox__switch checkbox__box"]')

next_step_element_selector=(By.XPATH, '//*[@class="gap--l"]//*[text()="Спасибо за регистрацию!"]')
error_data_selector = (By.XPATH, '//*[@class="jGrowl-message"]')

class RegistrationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://arnypraht.com/register/')

    def input_login(self):
        return self.find(input_login_selector)

    def send_keys_in_login(self, word):
        return self.input_login().send_keys(word)

    def input_password(self):
        return self.find(input_password_selector)

    def send_keys_in_password(self, word):
        return self.input_password().send_keys(word)

    def input_number(self):
        return self.find(input_number_selector)

    def send_keys_in_number(self, word):
        return self.input_number().send_keys(word)

    def button_enter(self):
        return self.find(button_enter_selector)

    def click_button_enter(self):
        return self.button_enter().click()

    def checkbox(self):
        return self.find(checkbox_selector)

    def click_checkbox(self):
        return self.checkbox().click()
    def choose_day_of_birth(self):
        self.find(date_day_selector).click()
        return self.find(date_day_input_selector).click()

    def choose_month_of_birth(self):
        self.find(date_month_selector).click()
        return self.find(date_month_input_selector).click()

    def choose_year_of_birth(self):
        self.find(date_year_selector).click()
        return self.find(date_year_input_selector).click()

    def choose_male_gender(self):
        self.find(male_gender_selector).click()

    def choose_female_gender(self):
        self.find(female_gender_selector).click()

    def is_data_correct(self):
        return self.find(next_step_element_selector).is_enabled()

    def is_data_incorrect(self):
        return self.find(error_data_selector).is_enabled()