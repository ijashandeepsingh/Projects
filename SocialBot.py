""" 
Prequisites required: selenium library installed in python root. 
This is a Instagram focused search py script that takes a notification and a search index. This script can also be modified for
searching various elements on other various platforms. (Tested over twitter).
"""



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
        bot.get("https://instagram.com/accounts/login/") # Login web link of the social site.
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
        
    def search_instagram(self, hashtag):   # method takes an object that is the user defined search index, in this case, a hashtag.
        bot = self.bot
        notification_box = bot.find_elements_by_class_name(name=) # to be filled accoding to class name defined by page script.
        notification_box.click()
        time.sleep(2)
        search_box = bot.find_elements_by_class_name(name=) # to be filled accoding to class name defined by page script.
        search_box.click()
        time.sleep(2)
        search_type = bot.find_elements_by_class_name("focus-visible")
        search_type.send_keys("#"+hashtag) 
        time.sleep(4)
        search_select = bot.find_element_by_partial_link_text("explore/tags/"+hashtag+"/")
        search_select.click()

    


"""****"""

mail = input("Enter the registered E-mail: ")
passw = getpass.getpass()
search = input("Enter the term to search:")
obj = SocialBot(mail, passw)
obj.login()
obj.search_instagram(hashtag=search)
