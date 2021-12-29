#!/usr/bin/env python

import glob
from selenium import webdriver



profiles_old=set(glob.glob('/tmp/rust_mozprofile*'))

browser=webdriver.Firefox()

profiles_new=set(glob.glob('/tmp/rust_mozprofile*'))

current_profile=(profiles_old.symmetric_difference(profiles_new))
print(current_profile)

browser.quit()
