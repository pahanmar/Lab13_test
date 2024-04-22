from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

go_to_waist_selector = (By.XPATH, '//*[@class="submenu__wrapper"]//*[@href="/category/waist-bags/"]')
go_to_big_selector = (By.XPATH, '//*[@class="submenu__wrapper"]//*[@href="/bags/bolshie-sumki/"]')
go_to_cherez_plecho_selector = (
By.XPATH, '//*[@class="submenu__wrapper"]//*[@href="/category/bags/sumki-cherez-plecho/"]')
button_filter_selector = (By.XPATH, '//*[@class="submenu__buttons"]//*[@class="button"]')
button_search_selector = (By.XPATH, '//*[@class="sign__absolute search-opened-invisible"]')
input_search_selector = (By.XPATH, '//*[@class="field__box field__box--input ui-autocomplete-input field__box--empty"]')
page_id=(By.XPATH, '//*[@class="spoiler__title"][text()="Большие сумки"]')


# Каркасная сумка с широким ремнем в цвете песочный-голубой


class BigBugsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://arnypraht.com/shop/')

    def go_to_waist_bugs(self):
        return self.find(go_to_waist_selector).click()

    def go_to_cherez_plecho(self):
        return self.find(go_to_cherez_plecho_selector).click()

    def is_page_correct(self):
        return self.find(page_id).is_enabled()