from selenium import webdriver
import base

driver = webdriver.Chrome()
driver.get(f'{base.cat_base}')

cat_button = driver.find_element_by_css_selector(base.cat_css_s)
cat_button.click()

def repeat():
    while 1==1:
        cat_button.click()

repeat()