from behave import given, then, when
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest


class UserAcc(unittest.TestCase):

    @given("User is at registration page")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=account/register")
        assert context.driver.title == "Register Account"

    @when("User fills all required fields")
    def step_impl(context):
        firstName = context.driver.find_element(By.CSS_SELECTOR, "#input-firstname")
        firstName.click()
        firstName.send_keys("Temp")

        lastName = context.driver.find_element(By.CSS_SELECTOR, "#input-lastname")
        lastName.click()
        lastName.send_keys("Nape")

        email = context.driver.find_element(By.CSS_SELECTOR, "#input-email")
        email.click()
        email.send_keys("Temp@gmail.com")

        phone = context.driver.find_element(By.CSS_SELECTOR, "#input-telephone")
        phone.click()
        phone.send_keys("777777777")

        address = context.driver.find_element(By.CSS_SELECTOR, "#input-address-1")
        address.click()
        address.send_keys("asdasf")

        city = context.driver.find_element(By.CSS_SELECTOR, "#input-city")
        city.click()
        city.send_keys("sdfasd")

        postCode = context.driver.find_element(By.CSS_SELECTOR, "#input-postcode")
        postCode.click()
        postCode.send_keys("654 21")

        country = Select(context.driver.find_element(By.CSS_SELECTOR, "#input-country"))
        country.select_by_visible_text("Cuba")

        region = context.driver.find_element(By.CSS_SELECTOR, "#input-zone")
        region.click()
        choice = context.driver.find_element(By.CSS_SELECTOR, "#input-zone > option:nth-child(2)")
        choice.click()

        password = context.driver.find_element(By.CSS_SELECTOR, "#input-password")
        password.click()
        password.send_keys("pass123456")

        confirm = context.driver.find_element(By.CSS_SELECTOR, "#input-confirm")
        confirm.click()
        confirm.send_keys("pass123456")

        agree = context.driver.find_element(By.CSS_SELECTOR,
                                            "#content > form > div > div > input[type=checkbox]:nth-child(2)")
        agree.click()

        submit = context.driver.find_element(By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
        submit.click()

    @then("User is registered")
    def step_impl(context):
        assert context.driver.title == "Your Account Has Been Created!"

    @given("User is not logged in")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=account/login")
        if (context.driver.title == "Account Login"):
            pass
        else:

            context.driver.find_element(By.CSS_SELECTOR,
                                        "#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md").click()
            context.driver.find_element(By.CSS_SELECTOR,
                                        "#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a").click()
            assert (context.driver.title == "Account Login")

    @given("User is registered1")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=account/register")
        firstName = context.driver.find_element(By.CSS_SELECTOR, "#input-firstname")
        firstName.click()
        firstName.send_keys("Temp")

        lastName = context.driver.find_element(By.CSS_SELECTOR, "#input-lastname")
        lastName.click()
        lastName.send_keys("Nape")

        email = context.driver.find_element(By.CSS_SELECTOR, "#input-email")
        email.click()
        email.send_keys("Temp@gmail.com")

        phone = context.driver.find_element(By.CSS_SELECTOR, "#input-telephone")
        phone.click()
        phone.send_keys("777777777")

        address = context.driver.find_element(By.CSS_SELECTOR, "#input-address-1")
        address.click()
        address.send_keys("asdasf")

        city = context.driver.find_element(By.CSS_SELECTOR, "#input-city")
        city.click()
        city.send_keys("sdfasd")

        postCode = context.driver.find_element(By.CSS_SELECTOR, "#input-postcode")
        postCode.click()
        postCode.send_keys("654 21")

        country = Select(context.driver.find_element(By.CSS_SELECTOR, "#input-country"))
        country.select_by_visible_text("Cuba")

        region = context.driver.find_element(By.CSS_SELECTOR, "#input-zone")
        region.click()
        choice = context.driver.find_element(By.CSS_SELECTOR, "#input-zone > option:nth-child(2)")
        choice.click()

        password = context.driver.find_element(By.CSS_SELECTOR, "#input-password")
        password.click()
        password.send_keys("pass123456")

        confirm = context.driver.find_element(By.CSS_SELECTOR, "#input-confirm")
        confirm.click()
        confirm.send_keys("pass123456")

        agree = context.driver.find_element(By.CSS_SELECTOR,
                                            "#content > form > div > div > input[type=checkbox]:nth-child(2)")
        agree.click()

        submit = context.driver.find_element(By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
        submit.click()

    @when("User fills credentials")
    def step_impl(context):
        context.driver.get("http://mys01.fit.vutbr.cz:8059/index.php?route=account/login")
        email = context.driver.find_element(By.CSS_SELECTOR, "#input-email")
        email.click()
        email.send_keys("Temp@gmail.com")

        password = context.driver.find_element(By.CSS_SELECTOR, "#input-password")
        password.click()
        password.send_keys("pass123456")

        context.driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(2) > div > form > input").click()

    @then("User is logged in")
    def step_impl(context):
        assert (context.driver.title == "My Account")

    @when("User clicks My Account -> Logout")
    def step_impl(context):
        context.driver.find_element(By.CSS_SELECTOR, "#top-links > ul > li.dropdown").click()
        context.driver.find_element(By.CSS_SELECTOR,
                                    "#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a").click()

    @then("User is logged out")
    def step_impl(context):
        assert (context.driver.title == "Account Logout")

    @given("User is logged in1")
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

