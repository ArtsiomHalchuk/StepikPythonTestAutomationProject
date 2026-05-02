from pages.base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_title()
        self.should_be_basket_breadcrumb()

    def should_be_basket_url(self):
        assert "/basket/" in self.browser.current_url, "Basket URL is not correct"

    def should_be_basket_title(self):
        assert "Basket" in self.browser.find_element(*BasketPageLocators.BASKET_TITLE).text

    def should_be_basket_breadcrumb(self):
        assert "Basket" in self.browser.find_element(*BasketPageLocators.BASKET_BREADCRUMB).text

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items are present in Basket , but should not be"

    def should_be_basket_empty_text(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text