import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Please read selenium documentation. You will need webdriver for your version of google chrome for this code to work as-is.

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.instagram.com/');
time.sleep(2)

username = ''
pw = ''

username_field = driver.find_element_by_class_name('f0n8F')
username_field.send_keys(username)

pw_field = driver.find_element_by_name('password')
pw_field.send_keys(pw)

time.sleep(2)

def Login():
    login_button = driver.find_element_by_tag_name('button.sqdOP.L3NKy.y3zKF')
    login_button.click()

    time.sleep(3)

def Notifications():
    notifications= driver.find_element_by_tag_name('button.aOOlW.HoLwm')
    notifications.click()

def Search():
    search = driver.find_element_by_class_name('XTCLo.x3qfX')
    search.send_keys('The White Stripes')
    time.sleep(2)
    search.send_keys(Keys.RETURN)
    search.send_keys(Keys.RETURN)
    time.sleep(3)


def First_post():
    firstPost = driver.find_element_by_class_name("v1Nh3.kIKUG._bz0w")
    firstPost.click()


def Like():
    like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    like.click()


def NextPost():
    nextPost = driver.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow')
    nextPost.click()



Login()
Notifications()
Search()
First_post()

i = 0
while i < 6:

    time.sleep(5)
    Like()
    time.sleep(3)
    NextPost()
    i+=1
