from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input_text = browser.find_element_by_id('answer')
    input_text.send_keys(y)
    button = browser.find_element_by_id('robotCheckbox')
    button.click()
    button1 = browser.find_element_by_id('robotsRule')
    button1.click()

    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
