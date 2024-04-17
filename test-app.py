import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope="session")
def browser():
    options = ChromeOptions()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "123.0",
        "selenoid:options": {
            "name": "Chrome Instance"
        }
    }
    browser = webdriver.Remote(
        command_executor=f"http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities, options=options)
    yield browser
    # Close the browser after each test function completes, or at the end of a session if scope was set to "session"
    browser.quit()

def test_google(browser):  
    # Now you use your 'browser' fixture as an argument in this test function
    browser.get('http://selenoid:80')
    sleep(10)
