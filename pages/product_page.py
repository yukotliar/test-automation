from pages.base_page import BasePage
from locators.locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.basket_button)
        basket_button.click()

    def should_be_correct_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name)
        added_to_basket_message = self.browser.find_element(*ProductPageLocators.added_to_basket_message)
        assert product_name.text in added_to_basket_message.text, "The message doesn't contain the product name"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.product_price)
        basket_total_price_message = self.browser.find_element(*ProductPageLocators.basket_total_price_message)
        assert product_price.text in basket_total_price_message.text, "The message contain wrong price"

