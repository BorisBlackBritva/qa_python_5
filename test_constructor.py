import constants
from locators import Locators
from constants import ConstantsLinks


def test_constructor_default_chapter_check(driver):
    driver.get(ConstantsLinks.MAIN_PAGE_LINK)
    bun_classes = driver.find_element(*Locators.BUN_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(bun_classes) == 7


def test_constructor_open_chapter_sauce_success(driver):
    driver.get(ConstantsLinks.MAIN_PAGE_LINK)
    driver.find_element(*Locators.SAUCE_CHAPTER_BUTTON).click()
    sauce_classes = driver.find_element(*Locators.SAUCE_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(sauce_classes) == 7


def test_constructor_open_chapter_filling_success(driver):
    driver.get(ConstantsLinks.MAIN_PAGE_LINK)
    driver.find_element(*Locators.FILLING_CHAPTER_BUTTON).click()
    filling_classes = driver.find_element(*Locators.FILLING_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(filling_classes) == 7


def test_constructor_open_chapter_bun_success(driver):
    driver.get(ConstantsLinks.MAIN_PAGE_LINK)
    driver.find_element(*Locators.FILLING_CHAPTER_BUTTON).click()
    driver.find_element(*Locators.FILLING_CHAPTER_BUTTON).get_attribute('class').split(' ')
    driver.find_element(*Locators.BUN_CHAPTER_BUTTON).click()
    bun_classes = driver.find_element(*Locators.BUN_CHAPTER_BUTTON).get_attribute('class').split(' ')

    assert len(bun_classes) == 7
