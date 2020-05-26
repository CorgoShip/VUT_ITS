import time
import unittest

from behave import given, then, when
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from behave import *


class ShoppingCartTest(unittest.TestCase):

    @when("User Clicks on Add to Cart")
    def addToCart(context):
        context.driver.find_element(By.ID, "button-cart").click()

    @given("User is viewing a {product}")
    def set_up(context, product):
        if product == "MacBook":
            context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&path=18&product_id=43")
        elif product == "MacBook Air":
            context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&path=18&product_id=44")
        else:
            context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&path=18&product_id=46")

    @then("Cart contains {product}")
    def step_impl(context, product, ):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=checkout/cart")
        temp = context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div/table/tbody/tr/td[3]")
        if product == "MacBook":
            assert temp.text == "Product 16"
        elif product == "MacBook Air":
            assert temp.text == "Product 17"
        else:
            assert temp.text == "Product 19"

    @given("User is viewing cart")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=checkout/cart")

    @given("Cart contains at least one product")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&path=18&product_id=43")
        context.driver.find_element(By.ID, "button-cart").click()

    @when("User clicks on Remove button on a product")
    def step_impl(context):
        element = context.driver.find_element(By.CSS_SELECTOR, ".btn-danger:nth-child(2)")
        actions = ActionChains(context.driver)
        actions.move_to_element(element).perform()
        element = context.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(context.driver)
        actions.move_to_element(element).perform()
        context.driver.find_element(By.CSS_SELECTOR, ".fa-times-circle").click()

    @then("Cart is empty")
    def step_impl(context):
        elem = context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p")
        assert elem.text == "Your shopping cart is empty!"

    @when("User changes Quantity of product to another number")
    def step_impl(context):
        elem = context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/input")
        elem.click()
        elem.send_keys("5")
        elem.send_keys(Keys.ENTER)

    @then("Quantity of product is the new number")
    def step_impl(context):
        time.sleep(2)
        elem = context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/input")
        assert elem.get_attribute("value") == "15"


