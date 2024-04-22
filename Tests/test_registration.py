import pytest
from selenium import webdriver
from Pages.registration_page import RegistrationPage

correct_login = ('mrrtdsfan@gmail.com')
correct_password = ('08df0sd53+8')
correct_number = ('88380615362')

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(100)
    return chrome_browser


def test_input_incorrect_data(browser):
    registration_page =RegistrationPage(browser)
    registration_page.open()
    registration_page.send_keys_in_login(correct_login)
    registration_page.send_keys_in_password(correct_password)
    registration_page.send_keys_in_number(correct_number)
    registration_page.choose_male_gender()
    registration_page.click_checkbox()
    registration_page.button_enter().click()
    assert registration_page.is_data_incorrect()

def test_input_correct_data(browser):
    registration_page =RegistrationPage(browser)
    registration_page.open()
    registration_page.send_keys_in_login(correct_login)
    registration_page.send_keys_in_password(correct_password)
    registration_page.send_keys_in_number(correct_number)
    registration_page.choose_male_gender()
    registration_page.click_checkbox()
    registration_page.choose_day_of_birth()
    registration_page.choose_month_of_birth()
    registration_page.choose_year_of_birth()
    registration_page.button_enter().click()
    assert registration_page.is_data_correct()

