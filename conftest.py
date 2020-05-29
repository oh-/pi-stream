"""
setting the default options for selenium
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.headless = True
    return webdriver.Firefox(
        options=options,
        firefox_binary='/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox-bin',
        executable_path="/Users/samuel/src/py/pi-stream/bin/geckodriver"
    )
