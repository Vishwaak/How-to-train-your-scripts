from selenium import webdriver
browser =webdriver.Chrome('/usr/bin/chromedriver')
browser.get('http://www.facebook.com/login')
try:
    elem = browser.find_element_by_id('email')
    elem.send_keys('') #Enter your Email
    password = browser.find_element_by_id('pass')
    password.send_keys('') #Enter your Password
    password.submit()
    print('Found <%s> element with that class name!' % (elem.tag_name))
    
except:
    print('Could not fill the login ')
    