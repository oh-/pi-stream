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

def test_home(browser):
    browser.get("http://localhost:5000/")
    assert "Python" in browser.title
    elem = browser.find_element_by_name("title")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in browser.page_source
    browser.close()
