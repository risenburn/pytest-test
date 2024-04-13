import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def test_google():  
	driver.get('https://www.google.com/')
	sleep(60)
	title = "Google"
	assert title == chrome_driver.title
	pageSource = chrome_driver.page_source
	gateway = "Our third decade of climate action"
	if not gateway in pageSource:
		pytest.fail( "Google Changed their Webpage")
	chrome_driver.close()


@pytest.fixture(scope='function')
def driver(request):
    basename = request.node.fspath.basename.split('.')[0]
    """Fixture for choose execution on local or selenoid driver"""
    selenoid_flag = request.config.getoption("--selenoid")
    if selenoid_flag:
        if request.param == 'Firefox':
            opts = FirefoxOptions()
            opts.add_argument("--width=1920")
            opts.add_argument("--height=1080")
            opts.accept_untrusted_certs = True
            capabilities = {
                "browserName": "firefox",
                "browserVersion": "124.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True,
                    "name": "Firefox Instance",
                    "videoName": f"{basename}-{request.param}.mp4"
                }
            }
            driver = webdriver.Remote(
                command_executor=f"http://{links.SELENOID_URL}:4444/wd/hub",
                desired_capabilities=capabilities, options=opts)
        elif request.param == 'Chrome':
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument('ignore-certificate-errors')
            capabilities = {
                "browserName": "chrome",
                "browserVersion": "123.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True,
                    "name": "Chrome Instance",
                    "videoName": f"{basename}-{request.param}.mp4"
                }
            }
            driver = webdriver.Remote(
                command_executor=f"http://{links.SELENOID_URL}:4444/wd/hub",
                desired_capabilities=capabilities, options=options)
        else:
            raise ValueError("Invalid driver type specified.")
    else:
        if request.param == 'Firefox':
            opts = FirefoxOptions()
            opts.add_argument("--width=1920")
            opts.add_argument("--height=1080")
            opts.accept_untrusted_certs = True
            driver = webdriver.Firefox(options=opts)
        elif request.param == 'Chrome':
            options = ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument('ignore-certificate-errors')
            driver = webdriver.Chrome(options=options)
        else:
            raise ValueError("Invalid driver type specified.")

    yield driver
    driver.quit()
