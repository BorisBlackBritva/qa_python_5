import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
import time


class TestRegistration:

    @pytest.mark.parametrize('name, email, password', [
        ['борис', 'тест@ътест.som', 'пароль'],
        ['BORIS', 'TEST@XTEST.som', 'PASSWORD'],
        ['Имя1', 'тестов@ътест.som', '1234567890'],
        ['Name1', 'login@XDOMEN.som', '!@#$%^&*()_+'],
        ['Борис Borisov#$% Borisovich11', 'грязнаяDUCK@ъсидойRICK.som', 'Пароль Password 123456 !@#$%^&*()']])
    def test_registration_positive(self, driver, name, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_PASSWORD))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_LINK_LOGIN_PAGE))

        attr_href = elem.get_attribute('href')

        assert attr_href == 'https://stellarburgers.nomoreparties.site/register'

    def test_registration_name_negative(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        name = ''
        email = 'notUsedEmail6667771111@notUsed.som'
        password = 'password'

        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_PASSWORD))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    @pytest.mark.parametrize('email', ['', 'notFormatEmail.slon'])
    def test_registration_email_negative(self, driver, email):
        driver.get('https://stellarburgers.nomoreparties.site/')
        name = 'Name'
        password = 'password'

        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_PASSWORD))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    @pytest.mark.parametrize('password', ['', '5symb'])
    def test_registration_password_negative(self, driver, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        name = 'Name'
        email = 'notUsedEmail6667771111@notUsed.som'

        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_PASSWORD))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
