from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[type="submit"].btn-add-to-basket')
    PRODUCT_GALLERY = (By.CSS_SELECTOR, "#product_gallery")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")