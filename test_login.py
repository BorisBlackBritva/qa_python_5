from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import ConstantsAuth, ConstantsLinks

class TestLogin:
    def test_login_main_page_success(self, driver):
        driver.get(ConstantsLinks.LOGIN_PAGE_LINK)
        driver.find_element(*Locators.RESTORE_PASSWORD_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.LOGIN_LINK_RESTORE_PASSWORD_PAGE)).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(ConstantsAuth.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(ConstantsAuth.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        make_order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_MAIN_PAGE_BUTTON)).text

        assert make_order_button_text == 'Оформить заказ'

    def test_login_via_personal_account_button_success(self, driver):
        driver.get(ConstantsLinks.MAIN_PAGE_LINK)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_LINK_LOGIN_PAGE))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(ConstantsAuth.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(ConstantsAuth.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        make_order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_MAIN_PAGE_BUTTON)).text

        assert make_order_button_text == 'Оформить заказ'

    def test_login_registration_page_success(self, driver):
        driver.get(ConstantsLinks.REGISTER_PAGE_LINK)
        driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_LINK_LOGIN_PAGE))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(ConstantsAuth.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(ConstantsAuth.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        make_order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_MAIN_PAGE_BUTTON)).text

        assert make_order_button_text == 'Оформить заказ'

    def test_login_restore_password_page_success(self, driver):
        driver.get(ConstantsLinks.LOGIN_PAGE_LINK)
        driver.find_element(*Locators.RESTORE_PASSWORD_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.LOGIN_LINK_RESTORE_PASSWORD_PAGE)).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(ConstantsAuth.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(ConstantsAuth.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        make_order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_MAIN_PAGE_BUTTON)).text

        assert make_order_button_text == 'Оформить заказ'
