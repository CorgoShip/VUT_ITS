from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def before_scenario(context, screario):
    context.driver = webdriver.Remote(command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub",
                                      desired_capabilities=DesiredCapabilities.FIREFOX)
    # context.driver = webdriver.Firefox(executable_path=r"C:\Users\Artic\Documents\VUT\ITS\proj2\geckodriver.exe")
    context.driver.implicitly_wait(15)


def after_scenario(context, scenario):
    context.driver.quit()
