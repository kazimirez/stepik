from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(int(time.time())))



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   'https://stepik.org/lesson/236897/step/1',
                                   'https://stepik.org/lesson/236898/step/1',
                                   'https://stepik.org/lesson/236899/step/1',
                                   'https://stepik.org/lesson/236903/step/1',
                                   'https://stepik.org/lesson/236904/step/1',
                                   'https://stepik.org/lesson/236905/step/1'
                                   ])
class TestLogin:
    def test_functional(self, browser, links):
        link = links
        browser.get(link)

        text_area = browser.find_element_by_css_selector(".string-quiz__textarea")
        text_area.send_keys(str(math.log(int(time.time()))))
        the_button = browser.find_element_by_css_selector(".submit-submission")
        the_button.click()

        the_hint = browser.find_element_by_css_selector(".smart-hints__hint")
        if the_hint.text == "Correct!":
            print('ok')
        else:
            print(the_hint.text)

