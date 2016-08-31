import os
import time
import urlparse
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import  sleep
import demjson
from DB import DB


class Browser(object):


    '''
        this class is for everything that will happen in the browser:
        - go to the yik yak website
        - go to my herd
        - copy the top 30 yaks above 50 upvotes
        - post yaks
        - upvote other peoples yaks.
    '''

    popular_schools_arr = []


    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.yikyak.com/nearby")

        self.db = DB()

    def login(self):
        current_url = self.browser.current_url
        if current_url == "https://www.yikyak.com/login?nextPath=%2Fnearby":
            self.browser.get("https://www.yikyak.com/login")
            sleep(1)
            self.browser.find_element_by_xpath("//*[@id=\"country\"]/option[3]").click()
            phoneNumber = raw_input("please input your mobile number: (+44) ")
            enterNumber = self.browser.find_element_by_xpath("//*[@id=\"phone\"]")
            enterNumber.send_keys(phoneNumber)
            # TODO: add an exception, if the number entered is not accepted by the website
            self.browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[2]/div/div/span/div/div/div/form/"
                                               "div[3]/button").click()

            self.browser.find_element_by_xpath(
                "//*[@id=\"app\"]/div/div/div/div[2]/div/div/span/div/div/div/form/div[2]"
                "/button").click()
            sleep(1)  # if this is not here it throws an eror when adding the pin
            # TODO: add an exceptiion for the pin not being accepted
            pin = raw_input("please input the 6 digit authenticate web pin: ")
            self.browser.find_element_by_xpath("//*[@id=\"pin\"]").send_keys(pin)
            sleep(1)  # if this is not here it throws an eror when adding the pin
            self.browser.find_element_by_xpath(
                "//*[@id=\"app\"]/div/div/div/div[2]/div/div/span/div/div/div/form/div[2]/"
                "button").click()

            # currently user has to manually click to allow the location settings
            # TODO: change so automatically allowes location settings.

        elif current_url == "https://www.yikyak.com/nearby":
            print "we are in to yik yak"
        else:
            print " not accepting it as a string"

    def get_world_top_yaks(self):
        # go to the top yaks page and scroll a few times, get any yak that has reached over 300 upvotes
        # or any that has avaraged over 65 upvotes per hours

        self.browser.get("https://www.yikyak.com/herds/104473")
        sleep(1)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        page_source = BeautifulSoup(self.browser.page_source, "html.parser")

        #for divs in page_source.find_all("div"):
         #   divClass = divs.get('class')
          #  if divClass == "message-main":

        divTag = page_source.find_all("div", {"class": "message-main"})

        for tag in divTag:

            includesImage = False

            messageDiv = tag.find_all("div", {"class": "message"})
            likes = tag.find_all("div", {"class": "like-md"}).getText()

            for div in messageDiv:

                for div in messageDiv:
                    children = div.findChildren()

                    for child in children:
                        classTag = child.get('class', [])

                        if classTag[0] == "content-image-container":
                            includesImage = True
                        # go to next div and download
                        else:
                            yak = child.getText()
                            # get the the string in the p tag.

            print "yak: " + yak + "\ttotal Likes: " + str(likes) + "\t has image:" + includesImage
            # send the data to the database using the database class.

            if includesImage:
                self.db.add_yak(yak, 'add teh image url here', likes)
            else:
                self.db.add_yak(yak, "null", likes)



    # def get_locations_top_yaks(self):
    #
    #     for school in self.popular_schools_arr:
    #         self.browser.get(school)





#//*[@id="app"]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[47]/div[1]/div[1]/div[1]/div[2]/div/div/div
#//*[@id="app"]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[47]/div[1]/div[1]/div[1]/div[2]/div/p
#//*[@id="app"]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[1]