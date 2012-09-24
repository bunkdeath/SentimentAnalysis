from com.data.GetDataLocation import GetDataLocation
#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

class Settings:
    def __init__(self):
        self.training_percent   = 100      # in 0 to 100 range
        self.testing_percent    = 20        # in 0 to 100 range
        
        data                    = GetDataLocation()
        data_path               = data.get_path()
        self.train_file         = data_path + "/svm.train"
        self.test_file          = data_path + "/svm.test"
        self.model_file         = data_path + "/model/svm.modeluni"
        self.dict_file          = data_path + "/svm.dictuni"
        self.pos_file           = data_path + "/svm.pos"
        self.neg_file           = data_path + "/svm.neg"
        self.stop_words_file    = data_path + "/stop"
        