#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
import urllib
import pycurl
import threading

class CrawlTweets(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.USER = "bunkdeath"
        self.PASS = "i1a4ukya1543"
        self.pf = {}

    def search(self, keyword):
        self.pf['track'] = keyword

        c = pycurl.Curl()
        c.setopt(pycurl.USERPWD, "%s:%s" % (self.USER, self.PASS))
        c.setopt(c.URL, 'https://stream.twitter.com/1/statuses/filter.json')
        c.setopt(c.POSTFIELDS, urllib.urlencode(self.pf))
        c.setopt(pycurl.WRITEFUNCTION, self.on_recieve)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)   
        c.setopt(c.VERBOSE, 1)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)

        c.perform()
        c.close()

    def on_recieve(self, data):
        self.queue.put(data)

    def run(self):
        self.search("tennis")