from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_product_page(self):
        self.should_be_product_gallery()
        self.should_be_product_description()
        self.should_be_price()
        self.should_be_add_to_basket()


    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to Basket button is not presented"
    def should_be_product_gallery(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_GALLERY), "Product gallery is not present"
    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Product description is not present"
    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Product price is not present"

    def should_be_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message_name, "Product name mismatch"

    def should_be_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_price, "Basket price mismatch"


