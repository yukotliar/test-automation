from pages.base_page import BasePage
from locators.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are present"

    def should_be_empty_basket_text(self):
        assert self.element_contains_text(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "The empty basket text isn't found in empty basket"
