import os

from com.bunkdeath.self.PreProcessing import HtmlCharacterConvert
from com.bunkdeath.self.data.GetDataLocation import GetDataLocation

class Prediction:
    def __init__(self):
        data = GetDataLocation()
        self.data_path = data.get_path()
        
        neg1  = open(os.path.join(self.data_path, "neg"), "r").read().lower().replace("'", "").splitlines()
        eneg  = open(os.path.join(self.data_path, "neg_emo"), "r").read().lower().replace("'", "").splitlines()
        hneg  = open(os.path.join(self.data_path, "neg_hash"), "r").read().lower().replace("'", "").splitlines()
        dneg  = open(os.path.join(self.data_path, "neg_n't"), "r").read().lower().replace("'", "").splitlines()
        oneg  = open(os.path.join(self.data_path, "neg_other"), "r").read().lower().replace("'", "").splitlines()
        sneg  = open(os.path.join(self.data_path, "neg_slang"), "r").read().lower().replace("'", "").splitlines()

        pos1  = open(os.path.join(self.data_path, "pos"), "r").read().lower().replace("'", "").splitlines()
        epos  = open(os.path.join(self.data_path, "pos_emo"), "r").read().lower().replace("'", "").splitlines()
        hpos  = open(os.path.join(self.data_path, "pos_hash"), "r").read().lower().replace("'", "").splitlines()
        opos  = open(os.path.join(self.data_path, "pos_other"), "r").read().lower().replace("'", "").splitlines()
        spos  = open(os.path.join(self.data_path, "pos_slang"), "r").read().lower().replace("'", "").splitlines()

        self.neg = neg1+oneg+dneg+sneg+hneg+eneg
        self.pos = pos1+opos+spos+hpos+epos
        self.decode = HtmlCharacterConvert()

        return

    def predict(self, tweet):
        # line : special html character decoded
        # sent : special character removed
        line, sent = self.pre_process(tweet)
        p = n = 0
        p, n, emos = self.emoticons(sent)
        for emo in emos:
            sent = sent.replace(emo, "")
        words = sent.split(" ")
        for word in words:
            if word in self.neg:
                n += 1
            elif word in self.pos:
                p += 1
            else:
                tok = word.split("-")
                for t in tok:
                    if t in self.neg:
                        n += 1
                    elif t in self.pos:
                        p += 1

        if p>n:
            return 1
        elif n>p:
            return -1
        else:
            return 0

    def analysis_word(self, word):
        if word in self.neg:
            return -1
        elif word in self.pos:
            return 1
        else:
            tok = word.split("-")
            for t in tok:
                if t in self.neg:
                    return -1
                elif t in self.pos:
                    return 1
        return 0

    def pre_process(self, tweet):
        line = self.decode.convert(tweet)
        sent = line.lower()
        sent = sent.replace("'", "")
        sent = sent.replace(".", "")
        sent = sent.replace("!", "")
        sent = sent.replace("?", "")
        sent = sent.replace("\"", "")

        return line, sent

    def emoticons(self, tweet):
        pemo = open(os.path.join(self.data_path, "pos_emo"), "r").read().splitlines()
        nemo = open(os.path.join(self.data_path, "neg_emo"), "r").read().splitlines()
        pos = 0
        neg = 0
        emos = []
        for emo in pemo:
            if (tweet.find(emo) != -1) or (tweet.lower().find(emo.lower()) != -1):
                pos += 1
                emos.append(emo)

        for emo in nemo:
            if (tweet.find(emo) != -1) or (tweet.lower().find(emo.lower()) != -1):
                neg += 1
                emos.append(emo)

        return pos, neg, emos

    def get_pos_neg_data(self):
        return self.pos, self.neg