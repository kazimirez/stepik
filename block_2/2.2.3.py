from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1").text

    num2 = browser.find_element_by_css_selector("#num2").text

    num1int = int(num1)
    num2int = int(num2)
    numsum = num1int + num2int
    thesum = str(numsum)
    select = Select(browser.find_element_by_tag_name("#dropdown"))
    select.select_by_value(thesum)
    thebutton = browser.find_element_by_css_selector(".btn-default") 
    thebutton.click()


    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()