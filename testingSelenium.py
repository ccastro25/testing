from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get("https://www.walmart.com/search?q=Milk&affinityOverride=store_led&facet=fulfillment_method%3APickup")
browser.page_source
#print(browser.title)