"""
setting the default options for selenium
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(
        options=options,
        firefox_binary='/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox-bin',
        executable_path="/Users/samuel/src/py/pi-stream/bin/geckodriver"
    )
    yield browser
    browser.close()
