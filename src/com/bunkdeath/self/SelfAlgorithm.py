from com.bunkdeath.self.data.GetDataLocation import GetDataLocation
from com.bunkdeath.self.Prediction import Prediction
import os

class SelfAlgorithm:
    def __init__(self):
        data = GetDataLocation()
        self.data_path = data.get_path()
        
        predict   = Prediction()
        self.pred = predict
        return

    def predict(self, tweet):
        predict = self.pred
        windowed_list = self.get_windowed_list(tweet)

        prediction = 0
        for lists in windowed_list:
            add = 0
            windowed_list_predict = ""
            for word in lists:
                predicted = predict.analysis_word(word)
                add += predicted
                windowed_list_predict += str(predicted) + " "

            weight = self.predict_windowed_list(windowed_list_predict.strip())
            prediction += weight

        if prediction == 0:
            prediction = predict.predict(tweet)

        if prediction < 0:
            return -1
        elif prediction > 0:
            return 1
        else:
            return 0

    def predict_windowed_list(self, prediction):
        rule = open(os.path.join(self.data_path, "rule")).read().splitlines()

        for line in rule:
            model, weight = line.split(":")
            weight = int(weight)
            if model == prediction:
                return weight

        return 0

    def apply_rule(self, list):
        
        return

    def get_windowed_list(self, tweet):
        self.window_size = 2
        words = tweet.split()
        windowed_list = []
        for i in range(len(words)-1):
            list = []
            list.append(words[i])
            list.append(words[i+1])
            windowed_list.append(list)

        return windowed_list

    def get_pos_neg_data(self):
        return self.pred.get_pos_neg_data()
