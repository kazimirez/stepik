import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
    browser.get(link)
    time.sleep(5)  # хватит и 5 я уверен
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
