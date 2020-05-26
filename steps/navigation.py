import time
import unittest

from behave import given, then, when
from nose.tools import assert_equal
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from behave import *


class NavigationTest(unittest.TestCase):

    @given("User is at eshop website")
    def setUp(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=common/home")
        assert context.driver.title == "Your Store"

    @when("User writes {product} to Search bar")
    def step_impl(context, product):
        context.driver.find_element(By.NAME, "search").click()
        context.driver.find_element(By.NAME, "search").send_keys(product)

    @when("Clicks search")
    def step_impl(context):
        context.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()

    @then("Webpage with result for {product} is displayed")
    def step_impl(context, product):
        assert context.driver.title != "404 Not Found"

    @when("Currency is set to {different}")
    def change_curr(context, different):
        context.driver.find_element(By.CSS_SELECTOR, ".btn > .hidden-xs").click()
        context.driver.find_element(By.NAME, different).click()

    @then("All prices are in {different}")
    def check_curr(context, different):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/product&product_id=40")
        text = context.driver.find_element(By.CSS_SELECTOR, "div.col-sm-4:nth-child(2) > ul:nth-child(4) > "
                                                            "li:nth-child(1) > h2:nth-child(1)").text
        if different == "GBP":
            assert text == "£98.63"
        elif different == "USD":
            assert text == "$123.20"
        else:  # EUR
            assert text == "113.95€"

    @given("Users is viewing {category}")
    def step_impl(context, category):
        if category == "Monitors":
            context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/category&path=25_28")
            assert context.driver.title == "Monitors"
        else:
            context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=product/category&path=33")
            assert context.driver.title == "Cameras"

    @when("Users clicks set Sort by to {sort}")
    def step_impl(context, sort):
        if sort == "Name (A - Z)":
            context.driver.find_element(By.ID, "input-sort").click()
            dropdown = context.driver.find_element(By.ID, "input-sort")
            dropdown.find_element(By.XPATH, "//option[. = 'Name (A - Z)']").click()
            context.driver.find_element(By.CSS_SELECTOR, "#input-sort > option:nth-child(2)").click()
        else:
            context.driver.find_element(By.ID, "input-sort").click()
            dropdown = context.driver.find_element(By.ID, "input-sort")
            dropdown.find_element(By.XPATH, "//option[. = 'Name (Z - A)']").click()
            context.driver.find_element(By.CSS_SELECTOR, "#input-sort > option:nth-child(3)").click()

    @then("{category} is sorted by {sort}")
    def step_impl(context, category, sort):
        if category == "Cameras":
            assert context.driver.current_url == "http://mys01.fit.vutbr.cz:8059/index.php?route=product/category&path=33&sort=pd.name&order=DESC"
        else:
            assert context.driver.current_url == "http://mys01.fit.vutbr.cz:8059/index.php?route=product/category&path=25_28&sort=pd.name&order=ASC"

    @when("User chooses {category}")
    def chooseCat(context, category):
        if category == "Cameras":
            context.driver.find_element(By.LINK_TEXT, "Cameras").click()
        elif category == "Tablets":
            context.driver.find_element(By.LINK_TEXT, "Tablets").click()
        else:
            elem1 = context.driver.find_element(By.CSS_SELECTOR, "li.dropdown:nth-child(3) > a:nth-child(1)")
            ActionChains(context.driver).move_to_element(elem1).perform()
            elem2 = context.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[2]/a")
            ActionChains(context.driver).move_to_element(elem1).perform()
            elem2.click()

    @then("{category} is shown")
    def CheckCat(context, category):
        if category == "Cameras":
            assert context.driver.title == "Cameras"
        elif category == "Tablets":
            assert context.driver.title == "Tablets"
        else:
            assert context.driver.title == "Monitors"
