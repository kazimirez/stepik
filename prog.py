from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")

print('Z')
print('anything')
print('anything2')
