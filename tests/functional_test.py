"""
Conventions for Python test discovery

pytest implements the following standard test discovery:

 - If no arguments are specified then collection starts from testpaths (if
   configured) or the current directory. Alternatively, command line arguments
   can be used in any combination of directories, file names or node ids.

 - Recurse into directories, unless they match norecursedirs.

 - In those directories, search for test_*.py or *_test.py files, imported by
   their test package name.

From those files, collect test items:

 - test prefixed test functions or methods outside of class
 - test prefixed test functions or methods inside Test prefixed test classes
   (without an __init__ method)
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def test_home():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        options=options,
        firefox_binary='/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox-bin',
        executable_path="/Users/samuel/src/py/pi-stream/bin/geckodriver"
    )
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
