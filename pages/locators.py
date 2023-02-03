from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "#login_form")
    login_email = (By.CSS_SELECTOR, "#id_login-username")
    login_password = (By.CSS_SELECTOR, "#id_login-password")
    login_button = (By.CSS_SELECTOR, "[name='login_submit']")

    register_form = (By.CSS_SELECTOR, "#register_form")
    register_email = (By.CSS_SELECTOR, "#id_registration-email")
    register_password_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    register_password_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    register_button = (By.CSS_SELECTOR, "[name='registration_submit']")