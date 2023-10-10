from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

def test_logout_success(driver, login):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_PERSONAL_ACCOUNT_BUTTON)).click()
    driver.get('https://stellarburgers.nomoreparties.site/')

    login_button_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_MAIN_PAGE_BUTTON)).text

    assert login_button_text == 'Войти в аккаунт'