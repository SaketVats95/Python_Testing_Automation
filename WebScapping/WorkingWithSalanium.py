from selenium import webdriver
"""browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('display-3')
    print('Found <%s> element with that class name!' % (elem.tag_name))
    myele=browser.find_element_by_link_text("online course of this book on Udemy")
    myele.click()
except:
    print('Was not able to find an element with that name.')
"""

link='https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
id='identifierId'

brower1=webdriver.Firefox()
brower1.get(link)

ele=brower1.find_element_by_id(id)

ele.send_keys('not_my_real_email')
ele_button_next=brower1.find_element_by_class_name("RveJvd")
ele_button_next.click()

