import os
import time
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

CURRENT_FILE_PATH = os.path.abspath(__file__)
DIR_PATH = os.path.dirname(CURRENT_FILE_PATH)
RESOURCES_PATH = os.path.join(DIR_PATH, '..', 'resources', )
DOWNLOAD_PATH = os.path.join(DIR_PATH, 'download')


def test_download_file_with_requests():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)
    PNG_PATH = os.path.join(DOWNLOAD_PATH, 'selenium_logo.png')
    r = requests.get(url)
    with open(PNG_PATH, 'wb') as file:
        file.write(r.content)
    size = os.path.getsize(PNG_PATH)
    assert size == 30803
    os.remove(PNG_PATH)


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
def test_download_file_with_browser():
    DOWNLOAD_FILE_PATH = os.path.join(DOWNLOAD_PATH, 'pytest-main.zip')
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": DOWNLOAD_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(1)
    size = os.path.getsize(DOWNLOAD_FILE_PATH)
    assert size == 1564360
    os.remove(DOWNLOAD_FILE_PATH)

