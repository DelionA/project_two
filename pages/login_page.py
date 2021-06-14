from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "login url incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "email login form not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "password login form not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "email register form not found"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), "password register form not found"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM), "password_confirm form not found"
        
        
