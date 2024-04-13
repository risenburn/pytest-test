import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def test_google():  
	browser.get('https://www.google.com/')
	sleep(60)
	title = "Google"
	assert title == chrome_driver.title
	pageSource = chrome_driver.page_source
	gateway = "Our third decade of climate action"
	if not gateway in pageSource:
		pytest.fail( "Google Changed their Webpage")
	chrome_driver.close()


@pytest.fixture(scope="session")
def browser():
	chrome_options = webdriver.ChromeOptions()
	browser = webdriver.Remote(
    	   command_executor='http://selenoid:4444/wd/hub',
    	   desired_capabilities={'browserName': 'chrome',
                          	'version': '123.0'},
    	   options=chrome_options)
 
	browser.maximize_window()
 
	yield browser
	browser.quit()
