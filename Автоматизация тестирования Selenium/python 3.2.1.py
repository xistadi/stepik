from selenium import webdriver
import unittest

class TestSystem(unittest.TestCase):

    def test_button(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        fn = browser.find_element_by_css_selector("input.first:required").send_keys("sergeeva")
        ln = browser.find_element_by_css_selector("input.second:required").send_keys("valeria")
        email = browser.find_element_by_css_selector("input.third:required").send_keys("sergeeva@trucker.group")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        congratulation = browser.find_element_by_css_selector("h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!', "test_button1")
        browser.quit()

    def test_button2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        fn = browser.find_element_by_css_selector("input.first:required").send_keys("sergeeva")
        ln = browser.find_element_by_css_selector("input.second:required").send_keys("valeria")
        email = browser.find_element_by_css_selector("input.third:required").send_keys("sergeeva@trucker.group")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        congratulation = browser.find_element_by_css_selector("h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!', "test_button2")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
