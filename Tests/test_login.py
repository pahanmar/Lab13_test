import pytest
from selenium import webdriver
from Pages.login_page import LoginPage

correct_login = ('xocipah897@togito.com')
correct_password = ('12345678')
incorrect_login = ('mater7sd')
incorrect_password = ('0ssdDfe34')


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(100)
    return chrome_browser


def test_input_correct_login_data(browser):
    login_page =LoginPage(browser)
    login_page.open()
    login_page.send_keys_in_login(correct_login)
    login_page.send_keys_in_password(correct_password)
    login_page.button_enter().click()
    assert login_page.is_data_correct()

 #Negotive test
def test_input_incorrect_login_data(browser):
    login_page =LoginPage(browser)
    login_page.open()
    login_page.send_keys_in_login(correct_login)
    login_page.send_keys_in_password(incorrect_password)
    login_page.button_enter().click()
    assert login_page.is_data_incorrect()