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


class WishListTest(unittest.TestCase):

    @given("User is logged in")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=account/login")
        if (context.driver.title == "Account Login"):
            email = context.driver.find_element(By.CSS_SELECTOR, "#input-email")
            email.click()
            email.send_keys("Temp@gmail.com")

            password = context.driver.find_element(By.CSS_SELECTOR, "#input-password")
            password.click()
            password.send_keys("pass123456")

            context.driver.find_element(By.CSS_SELECTOR,
                                        "#content > div > div:nth-child(2) > div > form > input").click()
        else:
            pass

    @when("User clicks Add product to Wish List")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&path=57&product_id=49")
        context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/button[1]/i").click()

    @then("Wish List contains the product")
    def step_impl(context):
        time.sleep(1)
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=account/wishlist")
        try:
            context.driver.find_element(By.CSS_SELECTOR,
                                        "#content > div.table-responsive > table > tbody > tr > td:nth-child(2) > a")
        except:
            assert False

    @given("Is at Wish List website")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=account/wishlist")

    @given("Wish List contains at least one product")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&path=57&product_id=49")
        context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/button[1]/i").click()

    @when("User cliks on Remove button on a product")
    def step_impl(context):
        time.sleep(1)
        context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/table/tbody/tr/td[6]/a").click()


    @then("Wish List is empty")
    def step_impl(context):
        elem = context.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/p")
        assert elem.text == "Your wish list is empty."


    @step("customer is viewing a product")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&path=57&product_id=49")