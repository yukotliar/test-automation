from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_BASKET_BUTTON = (By.CSS_SELECTOR, "[href*='basket']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages p:first-of-type")


class BasketPageLocators:
    # empty basket locators
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")

    # filled basket locators
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
