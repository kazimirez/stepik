from selenium import webdriver
import time
import math

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_css_selector("#treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    
    inputfield = browser.find_element_by_css_selector("#answer") 
    inputfield.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox") 
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule") 
    radiobutton.click()

    thebutton = browser.find_element_by_css_selector(".btn-default") 
    thebutton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()