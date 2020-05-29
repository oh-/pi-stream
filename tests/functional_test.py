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

def routes_home(browser):
    browser.get("http://localhost:5000/")

    #  Make sure that the name is in the title
    assert "pi-stream | Home" in browser.title

def routes_add(browser):
    browser.get("http://localhost:5000/add")
    #  Make sure that the name is in the title
    assert "add".upper() in browser.title.upper()

def routes_media_single(browser):
    #  open the page wiht a known media item
    browser.get("http://localhost:5000/media/123")
    assert "add".upper() in browser.title.upper()

def test_routes(browser):
    routes_home(browser)
    routes_add(browser)


def test_add_new_media(browser):
    browser.get("http://localhost:5000/add")
    #  assert 



