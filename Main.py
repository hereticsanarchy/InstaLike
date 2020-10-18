import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import tkinter as tk
import threading

driver = webdriver.Chrome()
driver.get('http://www.instagram.com/');
time.sleep(2)


root = tk.Tk()


class Main():

    def __init__(self, master):
        self.master = master
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.search = tk.StringVar()
        self.frame = tk.Frame(master, bg='#2f3157')
        self.frame.place(relwidth=1, relheight=1)
        self.button = tk.Button(self.frame, text='Get Likes', command=lambda: self.Threading())
        self.button.pack()
        self.User = tk.Entry(self.frame, textvariable=self.username)
        self.User.pack()
        self.Password = tk.Entry(self.frame, textvariable=self.password, show = '*')
        self.Password.pack()
        self.Search = tk.Entry(self.frame, textvariable=self.search)
        self.Search.pack()

    def printUser(self):
        return self.username.get()

    def printPass(self):
        return self.password.get()

    def printSearch(self):
        return self.search.get()





    def Credentials(self):
        username_field = driver.find_element_by_class_name('f0n8F')
        username_field.send_keys(self.printUser())

        pw_field = driver.find_element_by_name('password')
        pw_field.send_keys(self.printPass())

        time.sleep(5)

    def Login(self):
        login_button = driver.find_element_by_tag_name('button.sqdOP.L3NKy.y3zKF')
        login_button.click()

        time.sleep(3)

    def Notifications(self):
        notifications= driver.find_element_by_tag_name('button.aOOlW.HoLwm')
        notifications.click()

    def Search(self):
        search = driver.find_element_by_class_name('XTCLo.x3qfX')
        search.send_keys(self.printSearch())
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        search.send_keys(Keys.RETURN)
        time.sleep(3)


    def First_post(self):
        firstPost = driver.find_element_by_class_name("v1Nh3.kIKUG._bz0w")
        firstPost.click()


    def Like(self):

            try:
                like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                like.click()
            except NoSuchElementException:
                pass


    def NextPost(self):
        nextPost = driver.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow')
        nextPost.click()

    def Start(self):

        Main.Credentials(self)
        time.sleep(5)
        Main.Login(self)
        Main.Notifications(self)
        Main.Search(self)
        Main.First_post(self)

        i = 0
        while i < 499:

            time.sleep(5)
            Main.Like(self)
            time.sleep(20)
            Main.NextPost(self)
            i+=1

    def Threading(self):
        Thread = threading.Thread(target=self.Start())
        Thread.start()



app = Main(root)
root.wm_resizable(width=False, height=False)
root.geometry('400x200')


root.mainloop()
