import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_browser():
    browser.config.window_width = 1900
    browser.config.window_height = 1624
    browser.config.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.close()
