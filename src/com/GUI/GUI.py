#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Mar 16, 2012 7:05:43 AM$"


from com.GUI.ListModel import Person
from com.GUI.ListModel import ThingListModel
from com.GUI.ListModel import ThingWrapper
from com.GUI.ListModel import Controller
#from ListModel import TwitterFeedListModelling
#from SearchStream import Main
import os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtOpenGL
from PySide import QtDeclarative
import sys

class GUI:
    def __init__(self, crawl_tweets):
#        app = QApplication(sys.argv)
        self.path = os.path.dirname(__file__)
        dummy = os.path.join(self.path, "qml")
        self.main_qml = os.path.join(dummy, "focus.qml")

        controller = Controller()
        controller.set_crawl_tweet(crawl_tweets)
        things = [ThingWrapper(thing) for thing in []]

#        self.modelling = TwitterFeedListModelling()
#        self.view = self.modelling.model()


        self.view = QtDeclarative.QDeclarativeView()
        self.glw = QtOpenGL.QGLWidget()
        self.view.setViewport(self.glw)
        #self.view.setSource(os.path.join('qml','main.qml'))
        self.view.setSource(self.main_qml)


        self.twitterList = ThingListModel(things)

        self.view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
        self.view.setSource(self.main_qml)

        rc = self.view.rootContext()
        rc.setContextProperty('controller', controller)
        rc.setContextProperty('twitterListModel', self.twitterList)

        self.view.show()
#        self.view.showFullScreen()

#        sys.exit(app.exec_())

    def add(self, tweet, screenname, picURL, nb, mi, svm, sel):
        self.twitterList.addThings(ThingWrapper(Person(tweet, screenname, picURL, nb, mi, svm, sel)))