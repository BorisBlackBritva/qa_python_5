from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestPersonalAccount:
    def test_open_personal_account_success(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        logout_button_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_PERSONAL_ACCOUNT_BUTTON)).text

        assert logout_button_text == 'Выход'

    def test_open_constructor_from_personal_account_success(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        make_order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_MAIN_PAGE_BUTTON)).text

        assert make_order_button_text == 'Оформить заказ'