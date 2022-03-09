import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector(
        "#add_to_basket_form > button")

    time.sleep(5)
    assert button, 'Кнопка не найдена'