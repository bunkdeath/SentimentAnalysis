from com.sentimentanalysis.SentimentAnalysis import SentimentAnalysis
from com.GUI.GUI import GUI
from com.twitter.CrawlTweets import CrawlTweets
import Queue
import json
import threading

from PySide.QtCore import *
from PySide.QtGui import *
import sys

class AnalyseTweet(threading.Thread):
    '''
    It tries to analyse the tweet contained in queue and after analysing, puts it in gui
    '''
    def __init__(self, queue, gui):
        self.sentiment_analysis = SentimentAnalysis()
        threading.Thread.__init__(self)
        self.queue  = queue
        self.tweet  = ""
        self.count  = 0
        self.gui    = gui


        self.label      = {-1 : 'Negative', 1 : 'Positive', 0 : 'Neutral'}
        self.gradient   = {
                                "Positive" : ["#ddf3eb", "#49c5e0", "#2f606b"],
                                "Negative" : ["#7de235", "#49e083", "#456b2f"],
                                "Neutral"  : ["#e25d35", "#e09249", "#6b522f"]
                          }

    def parse_tweet(self, tweet):
        try:
            tweet_json = json.loads(tweet)
            for index in tweet_json:
                if index == 'text':
                    self.tweet = repr(tweet_json[index])
                    self.tweet = self.tweet[2:]
                    self.tweet = self.tweet[:len(self.tweet)-1]
            self.predict_and_add()
        except ValueError:
            print "Error : ", tweet
        return

    def predict_and_add(self):
        nb, mi, svm, sel = self.sentiment_analysis.predict(self.tweet)
        
        gradNB              = self.gradient[self.label[nb]]
        gradMI              = self.gradient[self.label[mi]]
        gradSVM             = self.gradient[self.label[svm]]
        gradSelf            = self.gradient[self.label[sel]]
        
        self.gui.add(self.tweet, "screenname", "picURL", gradNB, gradMI, gradSVM, gradSelf)

#printing tweet and their sentiment
        divider = '-' * (180)
        width = 10
        dict = {}
        dict["tweet"]       = self.tweet.ljust(100)
        dict["naivebayes"]  = self.label[nb].ljust(width)
        dict["maxint"]      = self.label[mi].ljust(width)
        dict["svm"]         = self.label[svm].ljust(width)
        dict["self"]        = self.label[sel].ljust(width)
        dict["divider"]     = divider

        print divider
        print "%(tweet)s\t %(naivebayes)s %(maxint)s %(svm)s %(self)s" % dict
#        print nb, mi, svm, sel
#        print self.tweet


    def run(self):
        while True:
            tweet = self.queue.get()
            self.parse_tweet(tweet)
            self.queue.task_done()


def main():
    app = QApplication(sys.argv)

    queue = Queue.Queue()

    t1 = CrawlTweets(queue)
    gui = GUI(t1)
#    t2 = AnalyseTweet(queue, gui)

    
#    t1.start()
#    t2.start()

    sys.exit(app.exec_())

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
