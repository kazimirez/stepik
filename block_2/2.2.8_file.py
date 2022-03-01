from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os 

os.path.abspath(os.path.dirname(__file__))
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '../file.txt')


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector(".form-control:nth-child(2)")
    first_name.send_keys("yyyy")

    second_name = browser.find_element_by_css_selector(".form-control:nth-child(4)")
    second_name.send_keys("yyyy")

    second_name = browser.find_element_by_css_selector(".form-control:nth-child(6)")
    second_name.send_keys("yyyy@fdfg.com")
    
    file_loader = browser.find_element_by_css_selector("#file")
    file_loader.send_keys(file_path)
    
    thebutton = browser.find_element_by_css_selector(".btn-primary") 
    thebutton.click()







finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()