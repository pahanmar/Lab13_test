from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

go_to_waist_selector = (By.XPATH, '//*[@class="submenu__wrapper"]//*[@href="/category/waist-bags/"]')
go_to_big_selector = (By.XPATH, '//*[@class="submenu__wrapper"]//*[@href="/bags/bolshie-sumki/"]')
go_to_cherez_plecho_selector = (By.XPATH, '//*[@class="submenu__wrapper"]//*[@href="/category/bags/sumki-cherez-plecho/"]')
button_filter_selector = (By.XPATH, '//*[@class="submenu__buttons"]//*[@class="button"]')
button_search_selector = (By.XPATH, '//*[@class="sign__absolute search-opened-invisible"]')
input_search_selector = (By.XPATH, '//*[@id="field-4"]')
button_show_all = (By.XPATH, '//*[@class="search-form__ac-btn iconed iconed--s"]')
search_result_selector = (By.XPATH, '//*[@href="#search-result-products"]//*[text()="1"]')
button_lava_color_selector = (By.XPATH, '//*[@data-swatch-sort="31"]//label')
filter_closer_selector = (By.XPATH, '//*[@class="cross"]')
filter_correct_selector = (By.XPATH, '//*[@class="shop-pager shop-pager--visible"]//*[text()=" / "]')
first_card_button_selector = (By.XPATH, '//*[@data-card-item="11959"]//span[@class="button__text"]')
button_keep_shopping_selector = (By.XPATH, '//*[@class="note__button-text"]')
button_go_to_the_basket = (By.XPATH, '//*[@href="/cart/"][@id="msMiniCart"]')
class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://arnypraht.com/shop/')

    def go_to_waist_bugs(self):
        return self.find(go_to_waist_selector).click()

    def go_to_big_bugs(self):
        return self.find(go_to_big_selector).click()

    def go_to_cherez_plecho_bugs(self):
        return self.find(go_to_cherez_plecho_selector).click()

    def send_keys_to_search(self, word):
        self.find(button_search_selector).click()
        return self.find(input_search_selector).send_keys(word)

    def click_show_all_button(self):
        self.find(button_show_all).click()

    def is_search_correct(self):
        return self.find(search_result_selector).is_enabled()

    def click_button_filter(self):
        return self.find(button_filter_selector).click()

    def choose_lava_color(self):
        self.find(button_lava_color_selector).click()

    def close_filter(self):
        self.find(filter_closer_selector).click()

    def check_filter_correctness(self):
        return self.find(filter_correct_selector).is_enabled()

    def add_first_item(self):
        self.find(first_card_button_selector).click()
        self.find(button_keep_shopping_selector).click()

    def go_to_the_basket(self):
        self.find(button_go_to_the_basket).click()