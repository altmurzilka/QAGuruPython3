import pytest
from selene import have, command
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    # browser.config.hold_browser_open = True
    # browser.open('https://demoqa.com/automation-practice-form')
    # browser.all('[id^=google_ads][id$=container__]').with_(timeout=5).wait_until(
    #     have.size_greater_than_or_equal(3)
    # )
    # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    yield
    browser.quit()
