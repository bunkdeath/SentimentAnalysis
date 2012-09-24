from com.data.GetDataLocation import GetDataLocation
class NaiveBayes:
    def __init__(self, n):
        data = GetDataLocation()
        self.data_path = data.get_path()
        
        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ',', '.',
            '<', '>', '?', '/']
        #train set data statistic
        #define positive and negative word training set
        #train set data statistic
        #positive word training set
        poslines = open(self.data_path+'/rt-polarity.pos', 'r').read().splitlines()
        #negative word training set
        neglines = open(self.data_path+'/rt-polarity.neg', 'r').read().splitlines()
        self.stop_list=open(self.data_path+'/stopwordslist_1.file','r').read().splitlines()
        #test_data=open(r'pos.txt','r').read().splitlines()
        self.poslinesTrain = poslines[:]
        self.neglinesTrain = neglines[:]

        #open the file for checking the emotions
        self.pos_smiley = open(self.data_path+'/positive_smile.pos', 'r').read().split()
        self.neg_smiley = open(self.data_path+'/negative_smile.neg', 'r').read().split()


        #create the train set and the test set by attaching labels to text to form a
        #list of tuples (sentence, label). Labels are 1 for positive, -1 for negative

        self.trainset = [(x, 1) for x in self.poslinesTrain] + [(x, -1) for x in self.neglinesTrain]
        self.poswords = {}#for storing the word count in unigram
        self.negwords = {}
        self.poswords_bigram = {}#for bigram
        self.negwords_bigram = {}
        self.poswords_ngram = {}#for n gram
        self.negwords_ngram = {}
        self.n = n
        self.train(self.n)

    def train(self, n):
        #train_count_unigram=1
        #train_count_bigram=1
        #train_count_ngram=1
        new_line_ngram = ''
        new_line_bigram = ''

        #common for all grams
        for line, label in self.trainset:
            #for removing the self.symbols if any:
            for ch in line:
                if ch in self.symbols:
                    line = line.replace(ch, ' ')
            line = line.lower()
            split_line = line.split()
            for count in range(len(line.split())):
                if split_line[count] in self.stop_list:
                    split_line[count]=split_line[count].replace(split_line[count],'')
            
            #to remove if any double spaces are occured
            new_line = ' '.join(split_line)
            new_line = new_line.split()
            length = len(new_line)
            #print length
            if self.n == 1:
                #train the unigram data
                for word in new_line:
                    #if train_count_unigram==1:
                        #   print 'Unigram training...'
                            #  train_count_unigram+=1
                    if label == 1:
                        self.poswords[word] = self.poswords.get(word, 0) + 1.0
                    else:
                        self.negwords[word] = self.negwords.get(word, 0) + 1.0

            elif self.n == 2:
                #Bigram Training
                #if train_count_bigram==1:
                    #   print 'Bigram Training...'
                for bigram_count in range(length):
                    #train_count_bigram+=1
                    if bigram_count == length-1:
                        continue
                    else:
                        new_line_bigram = ''.join(new_line[bigram_count]) + ' ' + ''.join(new_line[bigram_count + 1])
                        if label == 1:
                            self.poswords_bigram[new_line_bigram] = self.poswords_bigram.get(new_line_bigram, 0) + 1.0
                        else:
                            self.negwords_bigram[new_line_bigram] = self.negwords_bigram.get(new_line_bigram, 0) + 1.0
            else:
                #ngram training
                    #if train_count_ngram==1:

                        #  print self.n,' gram training...'
                    for ngram_count in range(length-n + 1):
                        #train_count_ngram+=1
                        if ngram_count == length-n + 1:
                            continue
                        else:
                            for n_count in range(n):
                                new_line_ngram = ''.join(new_line_ngram) + ' ' + ''.join(new_line[n_count + ngram_count])

                                if label == 1:
                                    self.poswords_ngram[new_line_ngram] = self.poswords_ngram.get(new_line_ngram, 0) + 1.0
                                else:
                                    self.negwords_ngram[new_line_ngram] = self.negwords_ngram.get(new_line_ngram, 0) + 1.0
                            #print self.poswords_ngram[new_line_ngram],' ',new_line_ngram
                        new_line_ngram = ''

    def set_up(self, tweets):
        return self.tweet
    def display_tweets(self, tweets):
        print 'The entered tweets is:; ', self.tweet
    def analyse(self, tweet):
        result = 0
        threshold_min = 6.0
        original_tweet = tweet
        #print 'THE ORIGINAL TWEET IS::'
        #print original_tweet
        tweet = tweet.lower()
        #check_for_emo(tweet)

        for ch in tweet:
            if ch in self.symbols:
                tweet = tweet.replace(ch, ' ')
                #remove if double spaces occured
        split_tweet = tweet.split()
        tweet = ' '.join(split_tweet)
        tweet = tweet.split()
        length=len(tweet)
        for count in range(length):
            if tweet[count] in self.stop_list:
                tweet[count]=tweet[count].replace(tweet[count],'')
        tweet=' '.join(tweet)
        tweet=tweet.split()
        tweet=' '.join(tweet)
        #print'The tweet after removal of stop words is:: ',tweet
        tweet=tweet.split() 
        length = len(tweet)
        
        if self.n == 1:
            #unigram training
            #train(1)
            poscount_unigram, negcount_unigram = 0.0, 0.0
            pos_training_count, neg_training_count = 0.0, 0.0
            sum_pos, sum_neg = 0.0, 0.0
            prob_pos, prob_neg = 0.0, 0.0
            percent_pos, percent_neg = 0.0, 0.0
            for count_words in range(len(tweet)):
                if len(tweet)==1:
                    sum_pos=self.poswords.get(tweet[0],0)+1.0
                    sum_neg=self.negwords.get(tweet[0],0)+1.0
                    percent_pos=(sum_pos/(sum_pos+sum_neg))*100
                    percent_neg=(sum_neg/(sum_neg+sum_pos))*100
                    if percent_pos-percent_neg>threshold_min:
                        poscount_unigram+=1
                    elif percent_neg-percent_pos>threshold_min:
                        negcount_unigram+=1
                    else:
                        poscount_unigram+=1
                        negcount_unigram+=1
                else:
                    sum_pos = self.poswords.get(tweet[count_words], 0) + 1.0
                    sum_neg = self.negwords.get(tweet[count_words], 0) + 1.0
                    #pos_training_count=self.poswords.get(self.tweet[count_words],0)+1.0
                    #neg_training_count=self.negwords.get(self.tweet[count_words],0)+1.0
                    sum_pos+=pos_training_count
                    #sum_neg+=neg_training_count
                    #print sum_pos, sum_neg
                    percent_pos = (sum_pos / (sum_pos + sum_neg)) 
                    percent_neg = (sum_neg / (sum_pos + sum_neg))
                                       
                    #print percent_pos,percent_neg
                    #print percent_pos-percent_neg
                    if percent_pos>percent_neg:
                        poscount_unigram+=1
                    elif percent_neg>percent_pos:
                        negcount_unigram+=1
                    else:
                        poscount_unigram+=1
                        negcount_unigram+=1
                    sum_pos = 0
                    sum_neg = 0

            prob_pos = poscount_unigram / (poscount_unigram + negcount_unigram)
            prob_neg = negcount_unigram / (poscount_unigram + negcount_unigram)
            #print prob_pos, prob_neg
            if prob_pos > prob_neg:
                result = 1
                #return result
                print '\n'
            if prob_neg > prob_pos:
                result = -1
                #return result
                print '\n'
            if prob_neg == prob_pos:
                result = 0
                #return result
        elif self.n == 2:
            #bigram training
            #train(2)
            poscount_bigram, negcount_bigram = 0.0, 0.0
            pos_training_bigram, neg_training_bigram = 0.0, 0.0
            sum_pos_bigram, sum_neg_bigram = 0.0, 0.0
            percent_pos_bigram, percent_neg_bigram = 0.0, 0.0
            prob_pos_bigram, prob_neg_bigram = 0.0, 0.0
            for bigram_count in range(length):
                if length == 1:
                    #this can be fixed easily for the final analysis part don't wory5
                    self.n=1
                    self.train(self.n )
                    pos_training_bigram = self.poswords.get(tweet[bigram_count], 0) + 1.0
                    neg_training_bigram = self.negwords.get(tweet[bigram_count], 0) + 1.0
                    sum_pos_bigram += pos_training_bigram
                    sum_neg_bigram += neg_training_bigram
                    #print sum_pos_bigram,sum_neg_bigram
                    percent_pos_bigram = (sum_pos_bigram / (sum_pos_bigram + sum_neg_bigram))*100
                    percent_neg_bigram = (sum_neg_bigram / (sum_neg_bigram + sum_pos_bigram))*100
                    if percent_pos_bigram-percent_neg_bigram>threshold_min:
                        poscount_bigram+=1
                    elif percent_neg_bigram-percent_pos_bigram>threshold_min:
                        negcount_bigram+=1
                    else:
                        percent_pos_bigram+=1
                        percent_neg_bigram+=1

                elif bigram_count == length-1:
                    continue
                else:
                    new_line_join = ''.join(tweet[bigram_count]) + ' ' + ''.join(tweet[bigram_count + 1])
                    pos_training_bigram = self.poswords_bigram.get(new_line_join, 0) + 1.0
                    #print 'try try try'
                    neg_training_bigram = self.negwords_bigram.get(new_line_join, 0) + 1.0
                # print neg_training_bigram
                    sum_pos_bigram += pos_training_bigram
                    sum_neg_bigram += neg_training_bigram
                    percent_pos_bigram = (sum_pos_bigram / (sum_pos_bigram + sum_neg_bigram)) 
                    percent_neg_bigram = (sum_neg_bigram / (sum_pos_bigram + sum_neg_bigram)) 

                    if percent_pos_bigram>percent_neg_bigram:
                        poscount_bigram+=2
                    elif percent_neg_bigram>percent_pos_bigram:
                        negcount_bigram+=2
                    else:
                        #done to avoid 0/0 case if occured
                        poscount_bigram+=1
                        negcount_bigram+=1
                        
                #print sum_pos_bigram,sum_neg_bigram
                sum_pos_bigram = 0.0
                sum_neg_bigram = 0.0
            if poscount_bigram==0 and negcount_bigram==0:
                poscount_bigram=1
                negcount_bigram=1
            prob_pos_bigram = poscount_bigram / (poscount_bigram + negcount_bigram)
            prob_neg_bigram = negcount_bigram / (poscount_bigram + negcount_bigram)
            if prob_pos_bigram > prob_neg_bigram:
                #print 'Tweet ', original_tweet
                result = 1
                #return result
               
            if prob_neg_bigram > prob_pos_bigram:
                #print 'Tweet ', original_tweet
                result = -1
                #return result
                
            if prob_neg_bigram == prob_pos_bigram:
                #print 'Tweet ', original_tweet
                result = 0
                #return result
        else:
            #ngram training
            #train(n)
            poscount_ngram, negcount_ngram = 0.0, 0.0
            pos_training_ngram, neg_training_ngram = 0.0, 0.0
            sum_pos_ngram, sum_neg_ngram = 0.0, 0.0
            percent_pos_ngram, percent_neg_ngram = 0.0, 0.0
            prob_pos_ngram, prob_neg_ngram = 0.0, 0.0
            new_string_ngram = ''
            #for ngram_count in range(len(tweet)-1):
            if len(tweet) == 1:
                #do the unigram training
                self.n=1
                self.train(self.n)
                pos_training_ngram = self.poswords.get(tweet[0], 0) + 1.0
                neg_training_ngram = self.negwords.get(tweet[0], 0) + 1.0
                sum_pos_ngram += pos_training_ngram
                sum_neg_ngram += neg_training_ngram
                percent_pos_ngram = (sum_pos_ngram / (sum_pos_ngram + sum_neg_ngram)) * 100
                percent_neg_ngram = (sum_neg_ngram / (sum_neg_ngram + sum_pos_ngram)) * 100
                if (percent_pos_ngram-percent_neg_ngram) > threshold_min:
                    poscount_ngram += 1
                elif (percent_neg_ngram-percent_pos_ngram) > threshold_min:
                    negcount_ngram += 1
                else:
                    poscount_ngram += 1
                    negcount_ngram += 1
            elif len(tweet) == 2:
                #do the bigram training
                self.n=2
                self.train(self.n)
                new_line_join = ''.join(tweet[0]) + ' ' + ''.join(tweet[1])
                pos_training_ngram = self.poswords_bigram.get(new_line_join, 0) + 1.0
                neg_training_ngram = self.negwords_bigram.get(new_line_join, 0) + 1.0
                sum_pos_ngram += pos_training_ngram
                sum_neg_ngram += neg_training_ngram
                precent_pos_ngram = (sum_pos_ngram / (sum_neg_ngram + sum_pos_ngram)) * 100
                percent_neg_ngram = (sum_neg_ngram / (sum_neg_ngram + sum_pos_ngram)) * 100
                if (percent_pos_ngram-percent_neg_ngram) > threshold_min:
                    poscount_ngram += 2
                elif (percent_neg_ngram-percent_pos_ngram) > threshold_min:
                    negcount_ngram += 2
                else:
                    poscount_ngram += 1
                    negcount_ngram += 1
            elif len(tweet) < self.n:
                print 'cannot process for this'
                exit
            else:
                #ngram training
                #train(n)
                for ngram_count in range(len(tweet)-1):
                    if ngram_count == len(tweet)-self.n + 1:
                        continue
                    else:
                        for n_count in range(self.n):
                            aa = n_count + ngram_count #temp variable
                            if aa >= len(tweet):
                                continue
                            else:
                                new_string_ngram = ''.join(new_string_ngram) + ' ' + ''.join(tweet[aa])
                    pos_training_ngram = self.poswords_ngram.get(new_string_ngram, 0) + 1.0
                    neg_training_ngram = self.negwords_ngram.get(new_string_ngram, 0) + 1.0
                    sum_pos_ngram += pos_training_ngram
                    sum_neg_ngram += neg_training_ngram
                    percent_pos_ngram = (sum_pos_ngram / (sum_pos_ngram + sum_neg_ngram)) * 100
                    percent_neg_ngram = (sum_neg_ngram / (sum_pos_ngram + sum_neg_ngram)) * 100
                    if percent_pos_ngram>percent_neg_ngram:
                        if percent_pos_ngram-percent_neg_ngram:
                          poscount_ngram+=self.n
                    elif percent_neg_ngram>percent_pos_ngram:
                        negcount_ngram+=self.n
                        
                    else:
                        #to avoid 0/0 case
                        poscount_ngram += 1
                        negcount_ngram += 1
                    new_string_ngram = ''
                # print sum_pos_ngram,sum_neg_ngram
                    sum_pos_ngram = 0.0
                    sum_neg_ngram = 0.0
            if poscount_ngram==0 and negcount_ngram==0:
                poscount_ngram=1
                negcount_ngram=1
            prob_pos_ngram = poscount_ngram / (poscount_ngram + negcount_ngram)
            prob_neg_ngram = negcount_ngram / (poscount_ngram + negcount_ngram)
            if prob_pos_ngram > prob_neg_ngram:
                #print 'ORIGINAL TWEET :: ', original_tweet
                result = 1
                #return result
                
            if prob_neg_ngram > prob_pos_ngram:
                #print 'ORIGINAL TWEET:: ', original_tweet
                result = -1
                #return result
                
            if prob_neg_ngram == prob_pos_ngram:
                #continue
                #print 'ORIGINAL TWEET:: ', original_tweet
                result = 0
                #return result
        return result
    def check_for_emo(self, tweet):
        tweet = tweet.split()
        result = 0
        poscount_emo,negcount_emo=0.0,0.0
        for count_smile in range(len(tweet)):
            #print tweet[count_smile]
            if tweet[count_smile] in self.pos_smiley:
                poscount_emo+=1
            elif tweet[count_smile] in self.neg_smiley:
                negcount_emo+=1
            else:
                poscount_emo+=1
                negcount_emo+=1
            if poscount_emo>negcount_emo:
                result=1
            elif negcount_emo>poscount_emo:
                result=-1
            elif poscount_emo==negcount_emo:
                result=3
            else:
                result=2
        return result


    def predict(self, tweet):
        naivebayes = NaiveBayes(1)
        result=naivebayes.check_for_emo(tweet)
        if result>2:
            result_unigram = naivebayes.analyse(tweet)
            naivebayes = NaiveBayes(2)
            result_bigram = naivebayes.analyse(tweet)
            naivebayse = NaiveBayes(3)
            result_trigram = naivebayse.analyse(tweet)
            if (result_unigram==result_bigram and result_unigram==result_trigram):
                result=result_unigram
            elif (result_unigram==result_bigram and result_bigram==result_trigram):
                result=result_unigram
            elif (result_unigram==result_bigram and result_bigram!=result_trigram):
                result=result_unigram
            elif (result_unigram==result_trigram and result_trigram!=result_bigram):
                result=result_unigram
            elif (result_bigram==result_trigram and result_trigram!=result_unigram):
                result=result_bigram
            elif (result_trigram==result_unigram and result_trigram!=result_bigram):
                result=result_unigram
            else:
                result=result_unigram
            print 'The result of the tweet is:: ',result
        elif result==2:
            print 'The result of the tweet is:: ',result-2
        else:
            print'The result of the tweet is:: ',result
        return
