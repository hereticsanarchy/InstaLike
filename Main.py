import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidElementStateException
import tkinter as tk
import threading




root = tk.Tk()


class Main():

    def __init__(self, master): #GUI and Variables
        self.master = master
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.search = tk.StringVar()
        self.frame = tk.Frame(master, bg='#2f3157')
        self.frame.place(relwidth=1, relheight=1)
        self.button = tk.Button(self.frame, text='Get Likes', command=lambda: self.Start())
        self.button.place(relx=.44,rely=.8)
        self.User = tk.Entry(self.frame, textvariable=self.username)
        self.User.place(relx = .53,rely=.2)
        self.Password = tk.Entry(self.frame, textvariable=self.password, show = '*')
        self.Password.place(relx = .53,rely=.32)
        self.Search = tk.Entry(self.frame, textvariable=self.search)
        self.Search.place(relx = .53,rely=.44)
        self.UserLabel = tk.Label(text = 'Username:', fg = 'white',bg ='#2f3157' )
        self.UserLabel.place(relx = .25,rely=.2)
        self.PassLabel = tk.Label(text='Password:', fg='white', bg='#2f3157')
        self.PassLabel.place(relx = .25,rely=.32)
        self.SearchLabel = tk.Label(text='Search Term:', fg='white', bg='#2f3157')
        self.SearchLabel.place(relx = .25,rely=.44)
        self.driver = webdriver.Chrome()

    def printUser(self): 
        return self.username.get()

    def printPass(self):
        return self.password.get()

    def printSearch(self):
        return self.search.get()

    def Credentials(self): #Pass user defined credentials to instagram

        self.driver.get('http://www.instagram.com/');
        time.sleep(2)

        username_field = self.driver.find_element_by_class_name('f0n8F')
        try:
            username_field.clear()
        except InvalidElementStateException:
            pass
        username_field.send_keys(self.printUser())

        pw_field = self.driver.find_element_by_name('password')
        try:
            pw_field.clear()
        except InvalidElementStateException:
            pass
        pw_field.send_keys(self.printPass())

        time.sleep(5)

    def Login(self):
        login_button = self.driver.find_element_by_tag_name('button.sqdOP.L3NKy.y3zKF')
        login_button.click()

        time.sleep(3)

    def Notifications(self): #Bypass notification screen if needed
        try:
            notifications= self.driver.find_element_by_tag_name('button.aOOlW.HoLwm')
            notifications.click()
        except NoSuchElementException:
            pass

    def Search(self): #Enter and search for user defined key word(s)
        search = self.driver.find_element_by_class_name('XTCLo.x3qfX')
        search.send_keys(self.printSearch())
        search.send_keys(Keys.RETURN)
        search.send_keys(Keys.RETURN)
        time.sleep(3)


    def First_post(self): #Click into first post
        firstPost = self.driver.find_element_by_class_name("v1Nh3.kIKUG._bz0w")
        firstPost.click()


    def Like(self): #Like if 'like' button is available, otherwise pass (in case of videos or images not loading)

            try:
                like = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                like.click()
            except NoSuchElementException:
                pass


    def NextPost(self):
        nextPost = self.driver.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow')
        nextPost.click()

    def Start(self): #Auto login and search

        Main.Credentials(self)
        Main.Login(self)
        Main.Notifications(self)
        Main.Search(self)
        Main.First_post(self)

        i = 0
        while i < 499:  # Like 1 image every 25 seconds, up to 500 images

            time.sleep(5)
            Main.Like(self)
            time.sleep(20)
            Main.NextPost(self)
            i+=1

    



app = Main(root)
root.wm_resizable(width=False, height=False) #Lock screen dimensions
root.geometry('400x200')
root.title('InstaLike Bot')


root.mainloop()
