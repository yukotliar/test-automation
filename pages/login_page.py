from pages.base_page import BasePage
from locators.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "The URL for login page is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), \
            "Login form is not presented on the login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), \
            "Register form is not presented on the login page"
