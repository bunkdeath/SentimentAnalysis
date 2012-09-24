from com.data.GetDataLocation import GetDataLocation
import math
import os

class MaximimEntropy:
    def __init__(self):
        data = GetDataLocation()
        self.data_path = data.get_path()
        
        self.pos_lines = open(os.path.join(self.data_path, 'rt-polarity.pos'),'r').read().splitlines()
        self.neg_lines = open(os.path.join(self.data_path, 'rt-polarity.neg'),'r').read().splitlines()

        #print num_lines_pos #total positive lines
        #print num_lines_neg #total neg lines
        pos_count = open(os.path.join(self.data_path, 'rt-polarity.pos'),'r').read().split()
        neg_count = open(os.path.join(self.data_path, 'rt-polarity.neg'),'r').read().split()
        
        self.pos_word_count = len(pos_count)
        self.neg_word_count = len(neg_count)

        self.trainset= [(x,1) for x in self.pos_lines] + [(x,-1) for x in self.neg_lines]

        self.pos_1gram = {}
        self.pos_2gram = {}
        self.pos_3gram = {}
        self.pos_4gram = {}
        self.pos_4gram = {}

        self.neg_1gram = {}
        self.neg_2gram = {}
        self.neg_3gram = {}
        self.neg_4gram = {}
        self.neg_5gram = {}
        self.train()
    def train(self):
       count = 0
       print "Training..."
       for line,label in self.trainset: #for every sentence and its label
#            print count
#            count += 1
            split_line=line.split()
            length=len(split_line)
            new_line=' '.join(split_line)
            new_line_split=new_line.split()
            length=len(new_line_split)
            for i in range(length):
                if label==1:
                        single_word=''.join(new_line_split[i])
                        self.pos_1gram[single_word]=self.pos_1gram.get(single_word,0)+1.0

                        if i!=length-1:
                            new_line_join=" ".join(new_line_split[i:i+2])
                            self.pos_2gram[new_line_join]=self.pos_2gram.get(new_line_join,0)+1.0
                        if i<length-2:
                            new_line_join1=" ".join(new_line_split[i:i+3])
                            self.pos_3gram[new_line_join1]=self.pos_3gram.get(new_line_join1,0)+1.0
                        if i<length-3:
                            new_line_join2=" ".join(new_line_split[i:i+4])
                            self.pos_4gram[new_line_join2]=self.pos_4gram.get(new_line_join2,0)+1.0
                        if i<length-4:
                            new_line_join3=" ".join(new_line_split[i:i+5])
                            self.pos_4gram[new_line_join3]=self.pos_4gram.get(new_line_join3,0)+1.0

                else:
                        single_word=''.join(new_line_split[i])
                        self.neg_1gram[single_word]=self.neg_1gram.get(single_word,0)+1.0
                        if i != length-1:
                            new_line_join=" ".join(new_line_split[i:i+2])
                            self.neg_2gram[new_line_join]=self.neg_2gram.get(new_line_join,0)+1.0
                        if i < length-2:
                            new_line_join1=" ".join(new_line_split[i:i+3])
                            self.neg_3gram[new_line_join1]=self.neg_3gram.get(new_line_join1,0)+1.0
                        if i<length-3:
                            new_line_join2= " ".join(new_line_split[i:i+4])
                            self.neg_4gram[new_line_join2]=self.neg_4gram.get(new_line_join2,0)+1.0
                        if i<length-4:
                            new_line_join3=" ".join(new_line_split[i:i+5])
                            self.neg_5gram[new_line_join3]=self.neg_5gram.get(new_line_join3,0)+1.0

       for k,v in self.pos_1gram.items():
           self.pos_1gram[k]=v/self.pos_word_count*math.log(self.pos_word_count/v,2)
       for k,v in self.neg_1gram.items():
           self.neg_1gram[k]=v/self.neg_word_count*math.log(self.neg_word_count/v,2)
       for k,v in self.pos_2gram.items():
           self.pos_2gram[k]=v/self.pos_word_count*math.log(self.pos_word_count/v,2)
       for k,v in self.neg_2gram.items():
           self.neg_2gram[k]=v/self.neg_word_count*math.log(self.neg_word_count/v,2)
       for k,v in self.pos_3gram.items():
           self.pos_3gram[k]=v/self.pos_word_count*math.log(self.pos_word_count/v,2)
       for k,v in self.neg_3gram.items():
           self.neg_3gram[k]=v/self.neg_word_count*math.log(self.neg_word_count/v,2)
       for k,v in self.pos_4gram.items():
           self.pos_4gram[k]=v/self.pos_word_count*math.log(self.pos_word_count/v,2)
       for k,v in self.neg_4gram.items():
           self.neg_4gram[k]=v/self.neg_word_count*math.log(self.neg_word_count/v,2)
       for k,v in self.pos_4gram.items():
           self.pos_4gram[k]=v/self.pos_word_count*math.log(self.pos_word_count/v,2)
       for k,v in self.neg_5gram.items():
           self.neg_5gram[k]=v/self.neg_word_count*math.log(self.neg_word_count/v,2)
       print "Completed"

    def analyse(self,tweet):
        #original_tweet=tweet
        #totpos, totneg = 0.0, 0.0

        tweet_tokens= tweet.split()
        tokens_length=len(tweet_tokens)

        pos_word_count_1gram = 0
        pos_word_count_2gram = 0
        pos_word_count_3gram = 0
        pos_word_count_4gram = 0
        pos_word_count_5gram = 0
        neg_word_count_1gram = 0
        neg_word_count_2gram = 0
        neg_word_count_3gram = 0
        neg_word_count_4gram = 0
        neg_word_count_5gram = 0

        for i in range(tokens_length):
                pos_word_count_1gram += self.pos_1gram.get(tweet_tokens[i],0)
                neg_word_count_1gram += self.neg_1gram.get(tweet_tokens[i],0)
                if i < tokens_length - 1:
                    dummy = " ".join(tweet_tokens[i:i+2])
                    pos_word_count_2gram += self.pos_2gram.get(dummy,0)
                    neg_word_count_2gram += self.neg_2gram.get(dummy,0)

                if i < tokens_length - 2:
                    dummy = " ".join(tweet_tokens[i:i+3])
                    pos_word_count_3gram += self.pos_3gram.get(dummy,0)
                    neg_word_count_3gram += self.neg_3gram.get(dummy,0)
                if i < tokens_length - 3:
                    dummy = " ".join(tweet_tokens[i:i+4])
                    pos_word_count_4gram += self.pos_4gram.get(dummy,0)
                    neg_word_count_4gram += self.neg_4gram.get(dummy,0)
                if i < tokens_length - 4:
                    dummy = " ".join(tweet_tokens[i:i+5])
                    pos_word_count_5gram += self.pos_4gram.get(dummy,0)
                    neg_word_count_5gram += self.neg_5gram.get(dummy,0)

        total_weighted_pos_count = pos_word_count_1gram + 100*pos_word_count_2gram + 100*pos_word_count_3gram + 100*pos_word_count_4gram + 100*pos_word_count_5gram
        total_weighted_neg_count = neg_word_count_1gram + 100*neg_word_count_2gram + 100*neg_word_count_3gram + 100*neg_word_count_4gram + 100*neg_word_count_5gram

        if(total_weighted_pos_count > total_weighted_neg_count):
            return 1
        elif(total_weighted_neg_count>total_weighted_pos_count):
            return -1
        else:
            return 0