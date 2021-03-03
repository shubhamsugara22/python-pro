import os
import pathlib
import unittest
from selenium import webdriver
# same can be used for firefox and ie
from webdriver_manager.chrome import ChromeDriverManager


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome(
    executable_path='C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe')


# class WebPageTest(unittest.TestCase):

#     def test_title:

#     def test_increase:

#     def test_decrease:
