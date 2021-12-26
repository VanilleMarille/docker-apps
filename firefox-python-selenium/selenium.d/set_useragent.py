#!/usr/bin/env python

from selenium import webdriver

profile=webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0")
driver=webdriver.Firefox(profile)
