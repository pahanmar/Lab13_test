from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

add_item_selector = (By.XPATH, '//*[@class="quantity__btn"]')
page_id = (By.XPATH, '//*[@class="pos__title"][text()="Итого к оплате"]')
clear_all_selector = (By.XPATH, '//*[@class="iconed iconed--clear"]')
basket_empty_check_selector = (By.XPATH, '//*[@class="h3"][text()="В вашей корзине пусто"]')


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://arnypraht.com/cart/')

    def is_page_correct(self):
        return self.find(page_id)

    def add_item(self):
        self.find(add_item_selector).click()

    def clear_basket(self):
        self.find(clear_all_selector).click()

    def is_basket_empty(self):
        return self.find(basket_empty_check_selector).is_enabled()