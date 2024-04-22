import pytest
from selenium import webdriver
from Pages.catalog_page import CatalogPage
from Pages.big_bugs_page import BigBugsPage
from Pages.waist_bugs_page import WaistBugsPage
from Pages.cherez_plecho_bugs_page import CherezPlechoBugsPage

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(100)
    return chrome_browser

def test_check_navigation(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open()
    catalog_page.go_to_big_bugs()
    big_bugs_page = BigBugsPage(browser)
    assert big_bugs_page.is_page_correct()
    big_bugs_page.go_to_waist_bugs()
    waist_page = WaistBugsPage(browser)
    assert waist_page.is_page_correct()
    waist_page.go_to_cherez_plecho()
    cherez_plecho_page = CherezPlechoBugsPage(browser)
    assert cherez_plecho_page.is_page_correct()

