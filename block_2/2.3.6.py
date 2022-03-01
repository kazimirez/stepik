from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    thebutton = browser.find_element_by_css_selector(".btn-primary") 
    thebutton.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    inputfield = browser.find_element_by_css_selector("#answer") 
    inputfield.send_keys(y)
    thebutton = browser.find_element_by_css_selector(".btn-primary") 
    thebutton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()