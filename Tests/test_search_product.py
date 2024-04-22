import pytest
from selenium import webdriver
from Pages.catalog_page import CatalogPage

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(100)
    return chrome_browser

def test_search_correct_product(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open()
    catalog_page.send_keys_to_search('Каркасная сумка с широким ремнем в цвете песочный-голубой')
    catalog_page.click_show_all_button()
    assert catalog_page.is_search_correct()