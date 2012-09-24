import os.path
from com.data.GetDataLocation import GetDataLocation
import htmlentitydefs
import os
import re
import collections

class HtmlCharacterConvert:
    def __init__(self):
        return

    def convert(self, text):
        try:
            mystring = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), text)
            return mystring.encode('utf-8')
        except:
            return text

class SpellCheck:
    def __init__(self):
        data = GetDataLocation()
        path = data.get_path()
        file_name = os.path.join(path, "spellcheck")

        self.NWORDS = self.train(self.words(file(file_name).read()))
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.pos = []
        self.neg = []
        return

    def words(self, text):
        return re.findall('[a-z]+', text.lower())

    def train(self, features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    def edits1(self, word):
       splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
       deletes    = [a + b[1:] for a, b in splits if b]
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
       replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
       inserts    = [a + c + b     for a, b in splits for c in self.alphabet]
       return set(deletes + transposes + replaces + inserts)

    def known_edits2(self, word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

    def known(self, words):
        return set(w for w in words if w in self.NWORDS)

    def correct(self, word):
        candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
        return max(candidates, key=self.NWORDS.get)
        return


class StopWords:
    def __init__(self):
        data = GetDataLocation()
        path = data.get_path()
        file_name = os.path.join(path, "stopwords")
        self.stop_word_list = open(file_name).read().splitlines()
        return

    def remove(self, tweet):
        words = tweet.split()
        sent = []
        for word in words:
            if word not in self.stop_word_list:
                sent.append(word)

        tweet = ""
        for word in sent:
            tweet += word + " "

        return tweet

class PreProcess:
    def __init__(self, pos, neg):
        self.stop_words = StopWords()
        self.spelling   = SpellCheck()
        self.html_char  = HtmlCharacterConvert()

        self.pos = pos
        self.neg = neg

    def pre_process(self, tweet):
        tweet = tweet.lower()
        tweet = self.stop_words.remove(self.html_char.convert(tweet))
        new = ""
        for word in tweet.split():
            sent = word.lower()
            sent = sent.replace("'", "")
            sent = sent.replace(".", "")
            sent = sent.replace("!", "")
            sent = sent.replace("?", "")
            sent = sent.replace("\"", "")
            if (sent not in self.pos) and (sent not in self.neg):
                new += self.spelling.correct(sent) + " "
            else:
                new += sent + " "

        return new