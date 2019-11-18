from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


class SocialBot:
    def __init__(self, email_id, password):
        self.email = email_id
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://instagram.com/accounts/login/")
        time.sleep(1)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        """Login Complete"""

    def search_instagram(self, hashtag):
        bot = self.bot
        notification_box = bot.find_elements_by_class_name(name="aOOlW   HoLwm")
        notification_box.click()
        time.sleep(2)
        search_box = bot.find_elements_by_class_name(name="pbgfb Di7vw")
        search_box.click()
        time.sleep(2)
        search_type = bot.find_elements_by_class_name("focus-visible")
        search_type.send_keys("#"+hashtag)
        time.sleep(4)
        search_select = bot.find_element_by_partial_link_text("explore/tags/"+hashtag+"/")
        search_select.click()



        #search_select.send_keys(Keys.RETURN)

        """"for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_id('placeholder')
            links = [elem.get_attribute("tweet") for elem in tweets]
            print(links)"""


"""****"""
# Function Call

u = input("Enter the registered E-mail: ")
p = getpass.getpass()
h = input("Enter the term to search:")
obj = SocialBot(u, p)
obj.login()
obj.search_instagram(hashtag=h)