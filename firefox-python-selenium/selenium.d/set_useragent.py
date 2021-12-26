#!/usr/bin/env python

from selenium import webdriver

profile=webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
driver=webdriver.Firefox(profile)
