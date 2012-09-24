import pickle

class BuildDictionaryBi:
    '''
        init creation dictionary
        usage
        CreateDirectory(train_file, dictionary_file)
        train_file -> file that contains training data set
        dictionary_file -> file where dictionary is to be written
    '''
    def __init__(self, train_file, dictionary_file):
        self.dict = {}
        self.train_file = train_file
        self.dictionary_file = dictionary_file

        self.count = {}
        self.start()
        return

    def build_count(self, word):
        current_count = self.dict[word]
        if current_count in self.count:
            self.count[current_count] += 1
        else:
            self.count[current_count] = 1
        return

    def build_dictionary(self, tweet, dict):
        words = tweet.split(" ")
	for i in range(0,len(words)-1):
            if words[i] in ["USERNAME","URL","EMAIL"]:
                continue
            if words[i+1] in ["USERNAME","URL","EMAIL"]:
                continue
            phrase = words[i] + " " + words[i+1]
            if phrase in dict:
                dict[phrase] += 1
            else:
                dict[phrase] = 1
	return dict

    def write_to_dictionary(self):
        dictionary = open(self.dictionary_file, "wb")
        pickle.dump(self.dict, dictionary)

    def start(self):
        lines = open(self.train_file, "r").read().splitlines()
        for line in lines:
            line = line.split(";;")
            tweet = line[1]
            self.dict = self.build_dictionary(tweet, self.dict)
        self.write_to_dictionary()
        return