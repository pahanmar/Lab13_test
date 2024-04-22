import pytest
from selenium import webdriver
from Pages.catalog_page import CatalogPage
from Pages.basket_page import BasketPage

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(100)
    return chrome_browser

def test_add_item_in_basket(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open()
    catalog_page.add_first_item()
    catalog_page.go_to_the_basket()
    baskeet_page = BasketPage(browser)
    assert baskeet_page.is_page_correct()

def test_edit_basket(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open()
    catalog_page.add_first_item()
    catalog_page.go_to_the_basket()
    baskeet_page = BasketPage(browser)
    assert baskeet_page.is_page_correct()
    baskeet_page.add_item()
    baskeet_page.clear_basket()
    assert baskeet_page.is_basket_empty()