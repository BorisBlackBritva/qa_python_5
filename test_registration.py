import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import ConstantsAuth, ConstantsLinks


class TestRegistration:

    @pytest.mark.parametrize('name, email, password', [
        [ConstantsAuth.NAME_VAL_1, ConstantsAuth.EMAIL_VAL_1, ConstantsAuth.PASSWORD_VAL_1],
        [ConstantsAuth.NAME_VAL_2, ConstantsAuth.EMAIL_VAL_2, ConstantsAuth.PASSWORD_VAL_2],
        [ConstantsAuth.NAME_VAL_3, ConstantsAuth.EMAIL_VAL_3, ConstantsAuth.PASSWORD_VAL_3],
        [ConstantsAuth.NAME_VAL_4, ConstantsAuth.EMAIL_VAL_4, ConstantsAuth.PASSWORD_VAL_4],
        [ConstantsAuth.NAME_VAL_5, ConstantsAuth.EMAIL_VAL_5, ConstantsAuth.PASSWORD_VAL_5]])
    def test_registration_positive(self, driver, name, email, password):
        driver.get(ConstantsLinks.REGISTER_PAGE_LINK)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.get(ConstantsLinks.REGISTER_PAGE_LINK)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        user_already_exist_error_text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.USER_ALREADY_EXIST_VALIDATION_ERROR)).text


        assert user_already_exist_error_text == "Такой пользователь уже существует"

    def test_registration_name_negative(self, driver):
        driver.get(ConstantsLinks.REGISTER_PAGE_LINK)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))
        driver.find_element(*Locators.INPUT_NAME).send_keys(ConstantsAuth.NAME_NOT_VAL_1)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(ConstantsAuth.EMAIL_VAL_NOT_USED)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(ConstantsAuth.PASSWORD_VAL_1)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert driver.current_url == ConstantsLinks.REGISTER_PAGE_LINK

    @pytest.mark.parametrize('email', [ConstantsAuth.EMAIL_NOT_VAL_1, ConstantsAuth.EMAIL_NOT_VAL_2])
    def test_registration_email_negative(self, driver, email):
        driver.get(ConstantsLinks.REGISTER_PAGE_LINK)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))
        driver.find_element(*Locators.INPUT_NAME).send_keys(ConstantsAuth.NAME_VAL_1)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(ConstantsAuth.PASSWORD_VAL_1)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert driver.current_url == ConstantsLinks.REGISTER_PAGE_LINK

    @pytest.mark.parametrize('password', [ConstantsAuth.PASSWORD_NOT_VAL_1, ConstantsAuth.PASSWORD_NOT_VAL_2])
    def test_registration_password_negative(self, driver, password):
        driver.get(ConstantsLinks.REGISTER_PAGE_LINK)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))
        driver.find_element(*Locators.INPUT_NAME).send_keys(ConstantsAuth.NAME_VAL_1)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(ConstantsAuth.EMAIL_VAL_NOT_USED)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert driver.current_url == ConstantsLinks.REGISTER_PAGE_LINK
