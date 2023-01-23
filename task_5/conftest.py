import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    browser.quit()
