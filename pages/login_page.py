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
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented on the login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented on the login page"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        register_button.click()
