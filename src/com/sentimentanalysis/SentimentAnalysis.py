from com.data.PreProcessing import PreProcess
from com.bunkdeath.self.SelfAlgorithm import SelfAlgorithm
from com.bunkdeath.svm.SVM import SVM
from com.nimesh.maxint.MaximumEntropy import MaximimEntropy
from com.bibek.naivebayes.NaiveBayes import NaiveBayes

class SentimentAnalysis:
    def __init__(self):
        self.tweet      = ""

        self.naivebayes = NaiveBayes(1)
        self.maxint     = MaximimEntropy()
        self.svm        = SVM()
        self.algorithm  = SelfAlgorithm()

        pos, neg        = self.algorithm.get_pos_neg_data()
        self.preprocess = PreProcess(pos, neg)
        return

    def data_preprocessing(self, tweet):
        self.tweet = self.preprocess.pre_process(tweet)

    def predict_naive_bayes(self):
        return self.naivebayes.analyse(self.tweet)

    def predict_maximum_entropy(self):
        return self.maxint.analyse(self.tweet)

    def predict_svm(self):
        return self.svm.predict(self.tweet)

    def predict_self_algorithm(self):
        return self.algorithm.predict(self.tweet)

    def predict(self, tweet):
        self.data_preprocessing(tweet)
        nb  = self.predict_naive_bayes()
        mi  = self.predict_maximum_entropy()
        svm = self.predict_svm()
        o   = self.predict_self_algorithm()

#        divider = '-' * (180)
#        width = 10
#        dict = {}
#        dict["tweet"]       = tweet.ljust(100)
#        dict["naivebayes"]  = self.label[nb].ljust(width)
#        dict["maxint"]      = self.label[mi].ljust(width)
#        dict["svm"]         = self.label[svm].ljust(width)
#        dict["self"]        = self.label[o].ljust(width)
#        dict["divider"]     = divider

#        print divider
#        print "%(tweet)s\t %(naivebayes)s %(maxint)s %(svm)s %(self)s" % dict

        return nb, mi, svm, o

#s = SentimentAnalysis()
#print
#print
#s.predict("nooot Good")
#s.predict("that movie i watched wasn't so gooood")
#s.predict("i am preety good")
#s.predict("hari is a baaad booy")
#s.predict("abinash is a bad boy")
#s.predict("i don't like the way that pradeep likes :( :) :D")
#s.predict("i got a new laptop :D")