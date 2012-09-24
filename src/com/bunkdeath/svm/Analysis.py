#! /usr/bin/python

import pickle

from com.bunkdeath.svm.Settings import Settings
from com.bunkdeath.svm.data.BuildDictionaryBi import BuildDictionaryBi
from com.bunkdeath.svm.data.BuildDictionaryUni import BuildDictionaryUni
from com.bunkdeath.svm.data.CreateTrainingTestingSet import CreateTrainingTestingSet
from com.bunkdeath.svm.libsvm.svmutil import *
from com.data.GetDataLocation import GetDataLocation

class Analysis:
    def __init__(self, settings = None, uni = True):
        if settings == None:
            self.settings = Settings()
        else:
            self.settings = settings

        self.training_percent   = self.settings.training_percent
        self.testing_percent    = self.settings.testing_percent
        self.training_file      = self.settings.train_file
        self.testing_file       = self.settings.test_file
        self.model_file         = self.settings.model_file
        self.dictionary_file    = self.settings.dict_file
        self.positive_set_file  = self.settings.pos_file
        self.negative_set_file  = self.settings.neg_file
        self.uni                = uni

        self.create_train_test_set()
        if(self.uni):
            self.build_unigram_dictionary()
        else:
            self.build_bigram_dictionary()
        self.train_and_test()
        return

    def create_train_test_set(self):
        print "starting to create train and test set"
        CreateTrainingTestingSet(self.training_percent, self.testing_percent,
                    self.training_file, self.testing_file, self.positive_set_file,
                    self.negative_set_file)
        print "finishing training and testing set file creation"
        return

    def build_unigram_dictionary(self):
        print "creating unigram dictionary"
        BuildDictionaryUni(self.training_file, self.dictionary_file)
        print "created unigram dictionary"
        return

    def build_bigram_dictionary(self):
        print "creating bigram dictionary"
        BuildDictionaryBi(self.training_file, self.dictionary_file)
        print "created bigram dictionary"
        return

    def train_and_test(self):
        print "test and train"
        TrainTest(self.settings, self.uni)
        print "finishing testing and training"
        return


class TrainTest:
    def __init__(self, settings, uni = True):
        if(uni):
            UniGram(settings)
        else:
            BiGram(settings)
        return


class UniGram:
    def __init__(self, settings):
        self.dictionary_filename = settings.dict_file
        self.model_filename = settings.model_file
        self.train_filename = settings.train_file
        self.test_filename = settings.test_file
        self.stop_words_file = settings.stop_words_file

        self.model = None
        self.dictionary = None
        self.stop_words = []

        self.load_dictionary()
#        self.load_stop_words()
        self.train_test()
        return

    def load_stop_words(self):
        words = open(self.stop_words_file,"r").read().splitlines()
        for word in words:

            self.stop_words.append(word)

        return

    def load_dictionary(self):
        dictfile = open(self.dictionary_filename)
        dict = pickle.load(dictfile)
        dictfile.close()

        # prepare word index
        i = 1
        self.idx = {}
        for key in dict:
            self.idx[key] = i
            i += 1

        self.dictionary = dict
        return

    def load_model(self):
        self.model = svm_load_model(model_file_name)
        return

    def create_model(self):
        return

    def train_test(self):
        file = open(self.train_filename,'r')
        linesTrain = file.read().splitlines()
        file.close()

        file = open(self.test_filename,'r')
        linesTest = file.read().splitlines()
        file.close()

        lines = linesTrain + linesTest

        dict = self.dictionary

        y = []
        x = []
        for line in lines:
            xi = {}
#            print line
            try:
                label, tweet = line.split(";;")
                words = tweet.split()
                label = int(label)
                if int(label) == 4:
                        label = 1
                elif int(label) == 0:
                        label = -1
                else:
                        continue
                y.append(label)
                for word in words:
                        if word not in dict:
                            continue
                        if word in self.stop_words:
                            continue

                        wordIdx = self.idx[word]
                        xi[wordIdx] = 1
    #                    xi[wordIdx] = xi.get(word, 0) + 1
                x.append(xi)
            except:
                print line.split(";;")


        fileNr = 0
        for i in [1]:
            c = 2 ** i
            try:
                param = '-s 0 -t 0 -h 0'
                fileNr += 1
                print "Training! Nr:", fileNr, param
                m = svm_train(y[0:len(linesTrain)], x[0:len(linesTrain)], param)
#                file = open("model" + str(fileNr), 'w')
                file = open(self.model_filename, 'w')
                svm_save_model(file.name, m)
                file.close()
                print "Training Done!"
                print

                print "Classifying"
                p_label, p_acc, p_val = svm_predict(y[len(linesTrain):], x[len(linesTrain):], m)
                print "Classification Done!"
                file = open("result", 'a')
                file.write(param + ";" + str(p_acc) + '\n')
                file.close()
            except:
                file = open("result", 'a')
                file.write(param + ";ERROR\n")
                file.close()
                continue


class BiGram:
    def __init__(self, settings):
        self.dictionary_file = settings.dict_file
        self.training_file = settings.train_file
        self.testing_file = settings.test_file
        self.model_file = settings.model_file

        self.dictionary = None
        self.model = None

        self.load_dictionary()
        self.train_test()
        return

    def load_dictionary(self):
        # load dictionary
        dictfile = open(self.dictionary_file)
        dict = pickle.load(dictfile)
        dictfile.close()
        "Done"
        print "total dict len = ", len(dict)
        # preprocess dictionary - delete low frequency words
        deList = []
        for key in dict:
                if dict[key] in [1,2,3,4,5]:
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

    def load_model(self):
        self.model = svm_load_model(self.model_file)
        return

    def train_test(self):
        file = open(self.training_file,'r')
        linesTrain = file.read().splitlines()
        file.close()

        file = open(self.testing_file,'r')
        linesTest = file.read().splitlines()
        file.close()

        dict = self.dictionary

        lines = linesTrain + linesTest

        y = []
        x = []
        for line in lines:
                xi = {}
                label, tweet = line.split(";;")
                words = tweet.split()
                label = int(label)
                if int(label) == 4:
                        label = 1
                elif int(label) == 0:
                        label = -1
                else:
                        continue
                y.append(label)
                for i in range(len(words)-1):
                        phrase = words[i] + " " + words[i+1]
                        if phrase not in dict:
                                continue
                        wordIdx = self.idx[phrase]
                        xi[wordIdx] = 1
                x.append(xi)

        fileNr = 0
        for i in [4]:
                c = 2**i
                try:
                        param = '-s 0 -t 0'
                        fileNr += 1
                        print "Training! Nr:",fileNr,param
                        m = svm_train(y[0:len(linesTrain)],x[0:len(linesTrain)],param)
                        file = open(self.model_file,'w')
                        svm_save_model(file.name,m)
                        #file.close()
                        print "Training Done!"

                        #m = svm_load_model('/result_models/SVMmodel2')
                        print "Classifying"
                        p_label,p_acc,p_val = svm_predict(y[len(linesTrain):],x[len(linesTrain):], m)
                        print "Classification Done!"
                        file = open("resultBigram",'a')
                        file.write(param+";"+str(p_acc)+'\n')
                        file.close()
                except:
                        file = open("resultBigram",'a')
                        file.write(param+";ERROR\n")
                        file.close()
                        continue
        return

class UseDataSet:
    def __init__(self, settings):
        self.dictionary_filename = settings.dict_file
        self.model_filename = settings.model_file
        self.train_filename = settings.train_file
        self.test_filename = settings.test_file

        self.model = None
        self.dictionary = None
        self.dict = None

        self.load_dictionary()
        self.load_wordnet()
        self.train_test()
        return

    def load_wordnet(self):
        dict = {}
        index = 1
        lines = open("data/data_set", "r").read().splitlines()
        for line in lines:
            tokens = line.split(" ")
            word = tokens[0]
            weight = abs(int(tokens[1]))
            dict[word] = [weight, index]
            index += 1

        self.dict = dict
        return

    def load_dictionary(self):
        dictfile = open(self.dictionary_filename)
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

    def load_model(self):
        self.model = svm_load_model(model_file_name)
        return

    def train_test(self):
        file = open(self.train_filename,'r')
        linesTrain = file.read().splitlines()
        file.close()

        file = open(self.test_filename,'r')
        linesTest = file.read().splitlines()
        file.close()

        lines = linesTrain + linesTest

        dict = self.dictionary

        y = []
        x = []
        for line in lines:
            xi = {}
            label, tweet = line.split(";;")
            words = tweet.split()
            label = int(label)
            if int(label) == 4:
                label = 1
            elif int(label) == 0:
                label = -1
            else:
                continue
            y.append(label)
            for word in words:
                if word in self.dict:
                    val = self.dict[word]
                    weight = val[0]
                    wordIdx = val[1]
                    xi[wordIdx] = weight
                    continue
                if word not in dict:
                    continue
                wordIdx = self.idx[word]
                xi[wordIdx] = 1
            x.append(xi)


        fileNr = 0
        for i in [1]:
            c = 2 ** i
            try:
                param = '-s 0 -t 0'
                fileNr += 1
                print "Training! Nr:", fileNr, param
                m = svm_train(y[0:len(linesTrain)], x[0:len(linesTrain)], param)
#                file = open("model" + str(fileNr), 'w')
                file = open(self.model_filename, 'w')
                svm_save_model(file.name, m)
                file.close()
                print "Training Done!"
                print

                print "Classifying"
                p_label, p_acc, p_val = svm_predict(y[len(linesTrain):], x[len(linesTrain):], m)
                print "Classification Done!"
                file = open("result", 'a')
                file.write(param + ";" + str(p_acc) + '\n')
                file.close()
            except:
                file = open("result", 'a')
                file.write(param + ";ERROR\n")
                file.close()
                continue





settings = Settings()

data = GetDataLocation()
data_path = data.get_path()

settings.training_percent   = 80      # in 0 to 100 range
settings.testing_percent    = 20        # in 0 to 100 range
settings.train_file         = data_path + "/svm.train"
settings.test_file          = data_path + "/svm.test"
settings.model_file         = data_path + "/model/svm.modeluni"
settings.dict_file          = data_path + "/svm.dictuni"
settings.pos_file           = data_path + "/svm.pos"
settings.neg_file           = data_path + "/svm.neg"
settings.stop_words_file    = data_path + "/stop"

run = Analysis(settings)
#run = Run(settings, False)