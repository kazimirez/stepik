from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    print(y)



    inputfield = browser.find_element_by_css_selector("#answer") 
    inputfield.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox") 
    checkbox.click()

    the_radio_button = browser.find_element_by_css_selector("#robotsRule") 
    browser.execute_script("return arguments[0].scrollIntoView(true);", the_radio_button)
    radiobutton = browser.find_element_by_css_selector("#robotsRule") 
    radiobutton.click()

    thebutton = browser.find_element_by_css_selector(".btn-primary") 
    thebutton.click()




    #answer

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()