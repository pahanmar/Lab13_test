import pytest
from selenium import webdriver
from Pages.catalog_page import CatalogPage

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(100)
    return chrome_browser

def test_check_filter_correctness(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open()
    catalog_page.click_button_filter()
    catalog_page.choose_lava_color()
    catalog_page.close_filter()
    assert catalog_page.check_filter_correctness()

