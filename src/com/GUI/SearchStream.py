#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Mar 27, 2012 7:50:33 AM$"


import json
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PySide.QtCore import *
from PySide.QtGui import *
import pycurl
import threading
import urllib


class Main(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pf = {}

    def run(self):
        print "start threading"
        USER = "bunkdeath"
        PASS = "i1a4ukya1543"
        c = pycurl.Curl()
        c.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
        c.setopt(c.URL, 'https://stream.twitter.com/1/statuses/filter.json')
        c.setopt(c.POSTFIELDS, urllib.urlencode(self.pf))
        c.setopt(c.VERBOSE, 1)
        c.setopt(pycurl.WRITEFUNCTION, self.on_receive)
        c.perform()
        c.close()

    def on_receive(self, tweet):
        print tweet
        self.parseStreamingTweet(tweet)

    def parseStreamingTweet(self, tweet):
        try:
            singleTweetJson = json.loads(tweet)
            twitter = Twitter()
            for index in singleTweetJson:
                if index == 'text':
                    tweet = repr(singleTweetJson[index])
                    twitter.setTweet(tweet)
                if index == 'user':
                    profilePic = singleTweetJson[index]['profile_image_url']
                    screenName = singleTweetJson[index]['screen_name']
                    twitter.setProfilePic(profilePic)
                    twitter.setScreenName(screenName)

            self.add_tweet(twitter)

        except ValueError:
            print "Error : ", tweet
            return

    def add_tweet(self, twitter):
        self.modelling.addTwitterFeed(twitter.tweet, twitter.screenName, twitter.profilePic, "#7de235", "#49e083", "#456b2f")

    def go(self, modelling):
        self.modelling = modelling
        self.start()

    def search(self, queryString):
        self.pf['track'] = queryString



class Twitter:
    def setTweet(self, tweet):
        self.tweet = tweet

    def setScreenName(self, screenName):
        self.screenName = screenName

    def setProfilePic(self, profilePic):
        self.profilePic = profilePic

    def setColor(self, color):
        if(color == "green"):
            self.top = "#7de235"
            self.mid = "#49e083"
            self.bot = "#456b2f"

        if(color == "red"):
            self.top = "#e25d35"
            self.mid = "#e09249"
            self.bot = "#6b522f"

        if(color == "blue"):
            self.top = "#ddf3eb"
            self.mid = "#49c5e0"
            self.bot = "#2f606b"