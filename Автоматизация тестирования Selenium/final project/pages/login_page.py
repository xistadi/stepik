from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        result = self.is_element_present('http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        assert result

    def should_be_login_form(self):
        result = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert result

    def should_be_register_form(self):
        result = self.is_element_present(*LoginPageLocators.REG_FORM)
        assert result

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        self.browser.get('http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        self.browser.find_element(*LoginPageLocators.REG_LOGIN).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()






