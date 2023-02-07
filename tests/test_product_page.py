from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo', [*range(7), pytest.param("7", marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_message()
    page.should_be_correct_price()
