import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.timeout = 4.0
    browser.driver.maximize_window()
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()

