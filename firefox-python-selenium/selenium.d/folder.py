#!/usr/bin/env python

import os
import glob
import subprocess
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#Select newest profile#
saved_profiles=(os.environ['HOME']) + '/.dockerapps/firefox-python-selenium/profiles'

profiles=os.listdir(saved_profiles)

profile_count=0
for profile in profiles:
	profile_count += 1


profile=(saved_profiles + "/profile_" + str(profile_count))
print("Selecting Profile: " + profile)
profile=webdriver.FirefoxProfile(profile)

#Configure selenium#
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.set_preference("network.cookie.cookieBehavior", 1)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

options=webdriver.FirefoxOptions()

#Start selenium#
profiles_old=set(glob.glob('/tmp/rust_mozprofile*'))

browser=webdriver.Firefox(options=options, firefox_profile=profile, desired_capabilities=desired) 

profiles_new=set(glob.glob('/tmp/rust_mozprofile*'))

current_profile=(profiles_old.symmetric_difference(profiles_new))
for convert in current_profile:
	current_profile=convert

#Save new profile and quit selenium#
input("Press any key to save new profile")

profile_count += 1
save_to_profiles=(saved_profiles + "/profile_" + str(profile_count)) 
print(save_to_profiles)
subprocess.run(["cp", "-r", current_profile, save_to_profiles]) 

browser.quit()
