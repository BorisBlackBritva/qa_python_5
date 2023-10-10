import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    email = Constants.email
    password = Constants.password

    driver.get('https://stellarburgers.nomoreparties.site/login')
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_LINK_LOGIN_PAGE))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_ORDER_MAIN_PAGE_BUTTON))

