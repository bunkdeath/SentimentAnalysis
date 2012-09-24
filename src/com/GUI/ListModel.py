import os.path
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="root"
__date__ ="$Apr 26, 2012 7:47:11 AM$"

from PySide import QtCore
from PySide import QtDeclarative
from PySide.QtCore import QModelIndex

class ThingWrapper(QtCore.QObject):
    changed = QtCore.Signal()
    
    def __init__(self, thing):
        QtCore.QObject.__init__(self)
        self._thing = thing
        
    @QtCore.Property(str, notify=changed)
    def tweet(self):
        return self._thing.tweet

    @QtCore.Property(str, notify=changed)
    def sentimentColor(self):
        return self._thing.color

    @QtCore.Property(str, notify=changed)
    def screenName(self):
        return self._thing.screenName

    @QtCore.Property(str, notify=changed)
    def profilePicURL(self):
        return self._thing.profilePic

    @QtCore.Property(str, notify=changed)
    def gradientTop(self):
        return self._thing.gradientTop

    @QtCore.Property(str, notify=changed)
    def gradientMid(self):
        return self._thing.gradientMid

    @QtCore.Property(str, notify=changed)
    def gradientBot(self):
        return self._thing.gradientBot

    @QtCore.Property(str, notify=changed)
    def nbgrad1(self):
        return self._thing.nbgrad1

    @QtCore.Property(str, notify=changed)
    def nbgrad2(self):
        return self._thing.nbgrad2

    @QtCore.Property(str, notify=changed)
    def nbgrad3(self):
        return self._thing.nbgrad3

    @QtCore.Property(str, notify=changed)
    def migrad1(self):
        return self._thing.migrad1

    @QtCore.Property(str, notify=changed)
    def migrad2(self):
        return self._thing.migrad2

    @QtCore.Property(str, notify=changed)
    def migrad3(self):
        return self._thing.migrad3

    @QtCore.Property(str, notify=changed)
    def svmgrad1(self):
        return self._thing.svmgrad2

    @QtCore.Property(str, notify=changed)
    def svmgrad2(self):
        return self._thing.svmgrad2

    @QtCore.Property(str, notify=changed)
    def svmgrad3(self):
        return self._thing.svmgrad3

    @QtCore.Property(str, notify=changed)
    def selfgrad1(self):
        return self._thing.selfgrad1

    @QtCore.Property(str, notify=changed)
    def selfgrad3(self):
        return self._thing.selfgrad1

    @QtCore.Property(str, notify=changed)
    def selfgrad3(self):
        return self._thing.selfgrad1



class ThingListModel(QtCore.QAbstractListModel):
    COLUMNS = ('thing', )

    def __init__(self, things):
        QtCore.QAbstractListModel.__init__(self)
        self._things = things
        self.setRoleNames(dict(enumerate(ThingListModel.COLUMNS)))

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._things)

    def data(self, index, role):
        if index.isValid() and role == ThingListModel.COLUMNS.index('thing'):
            return self._things[index.row()]
        return None

    def addThings(self,things):
        row = len(self._things)
        if len(self._things):
# comment next line if not working
            self.beginInsertRows(QModelIndex(), 0, 0)
            self._things.insert(0, things)
# comment next line if not working
            self.endInsertRows()
#            self._things.insert(row+1, things)
        else:
            self._things.append(things)
#        self.reset()

class Controller(QtCore.QObject):
    @QtCore.Slot(QtCore.QObject)
    def thingSelected(self, wrapper):
        print 'Tweet : ', wrapper._thing.tweet


class Person(object):
    def __init__(self, tweet, screenName, pic, nb, mi, svm, sel):
        self.tweet = tweet
        self.screenName = screenName
        self.profilePic = pic

        self.nbgrad1, self.nbgrad2, self.nbgrad3 = nb

        self.migrad1, self.migrad2, self.migrad3 = mi

        self.svmgrad1, self.svmgrad2, self.svmgrad3 = svm

        self.selfgrad1, self.selfgrad2, self.selfgrad3 = sel