import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope="session")
def browser():
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Remote(
           command_executor='http://0.0.0.0:4444/wd/hub',
           desired_capabilities={'browserName': 'chrome',
                                  'version': '123.0'},
           options=chrome_options)
 
    browser.maximize_window()
 
    # This is where you yield the browser instance, allowing it to be used in tests
    yield browser
    # Close the browser after each test function completes, or at the end of a session if scope was set to "session"
    browser.quit()

def test_google(browser):  
    # Now you use your 'browser' fixture as an argument in this test function
    browser.get('https://www.google.com/')
    sleep(60)
    assert "Google" == browser.title
    pageSource = browser.page_source
    gateway = "Our third decade of climate action"
    if not gateway in pageSource:
        pytest.fail( "Google Changed their Webpage")
