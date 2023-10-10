from locators import Locators

def test_change_constructor_chapter_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    bun_classes = driver.find_element(*Locators.BUN_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(bun_classes) == 7

    driver.find_element(*Locators.SAUCE_CHAPTER_BUTTON).click()
    sauce_classes = driver.find_element(*Locators.SAUCE_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(sauce_classes) == 7

    driver.find_element(*Locators.FILLING_CHAPTER_BUTTON).click()
    filling_classes = driver.find_element(*Locators.FILLING_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(filling_classes) == 7

    driver.find_element(*Locators.BUN_CHAPTER_BUTTON).click()
    bun_classes = driver.find_element(*Locators.BUN_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(bun_classes) == 7

