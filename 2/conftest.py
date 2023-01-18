import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def config_chrome():
    options = Options()
    # options.add_argument('chrome')  # Use headless if you do not need a browser UI
    # options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options

# Analog
# @pytest.fixture(scope="class")
# def open_browser():
#     browser.config.window_height = 950
#     browser.config._window_width = 1600


@pytest.fixture()
def web_driver_config(config_chrome):
    browser.config.driver = webdriver.Chrome(options=config_chrome)
    return browser.config.driver


@pytest.fixture()
def open_browser(web_driver_config):
    browser.open('https://google.com')
    yield