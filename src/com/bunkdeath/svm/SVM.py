#! /usr/bin/python

import pickle

from com.bunkdeath.svm.Settings import Settings
from com.bunkdeath.svm.libsvm.svmutil import svm_load_model
from com.bunkdeath.svm.libsvm.svmutil import svm_predict_one

class SVM:
    def __init__(self, settings = None):
        if settings == None:
            settings = Settings()


        self.model_file         = settings.model_file
        self.dictionary_file    = settings.dict_file
        self.model              = None

        self.load_dictionary()
        self.load_model()
        return

    def load_dictionary(self):
        dictfile = open(self.dictionary_file)
        dict = pickle.load(dictfile)
        dictfile.close()

        # preprocess dictionary - delete low frequency words
        deList = []
        for key in dict:
            if dict[key] in range(1, 7):
                deList.append(key)
        for item in deList:
            del dict[item]

        # prepare word index
        i = 1
        self.idx = {}
        for key in dict:
            self.idx[key] = i
            i += 1

        self.dictionary = dict
        return

    def process_tweet(self, tweet):
        dict = self.dictionary
        x = []
        xi = {}
        words = tweet.lower().split()
        for word in words:
            if word not in dict:
                continue
            wordIdx = self.idx[word]
            xi[wordIdx] = 1
        x.append(xi)
        return x

    def predict(self, tweet):
        x = self.process_tweet(tweet)
        p_label, p_val = svm_predict_one(x, self.model)

        percent_bias = 10.0/100

        result = abs(p_val[0])-percent_bias
        if(result==0 or result < 0):
            return 0
        return int(p_label)

    def load_model(self):
        self.model = svm_load_model(self.model_file)
        return