from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.get('https://gabrielecirulli.github.io/2048/')
keysTuple = (keys.Keys.ARROW_UP, keys.Keys.ARROW_RIGHT, keys.Keys.ARROW_DOWN,keys.Keys.ARROW_LEFT)
actions = action_chains.ActionChains(browser)
while True:
    actions = action_chains.ActionChains(browser)
    actions.send_keys(keysTuple).perform()
    
    
   