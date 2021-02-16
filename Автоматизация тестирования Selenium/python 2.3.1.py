from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()  # нажимаем ок для алерта

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input_text = browser.find_element_by_id('answer')
    input_text.send_keys(y)

    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
