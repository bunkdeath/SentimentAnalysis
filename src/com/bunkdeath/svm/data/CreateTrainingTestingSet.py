#! /usr/bin/python

class CreateTrainingTestingSet:
    def __init__(self, percent_training, percent_testing,
                training_file = "train", testing_file = "test",
                positive_set_file = "pos", negative_set_file = "neg"):
        self.per_train = (percent_training * 1.0) / 100
        self.per_test  = (percent_testing * 1.0) / 100
        self.positive_set_file = positive_set_file
        self.negative_set_file = negative_set_file
        self.training_file = training_file
        self.testing_file = testing_file

        self.start()
        return

    def start(self):
        pos = open(self.positive_set_file, "r").read().splitlines()
        neg = open(self.negative_set_file, "r").read().splitlines()

        total_pos = len(pos)
        total_neg = len(neg)

        pos_rand_train = []
        neg_rand_train = []
        pos_rand_test  = []
        neg_rand_test  = []

        train_pos = int(total_pos*self.per_train)
        train_neg= int(total_neg*self.per_train)
        test_pos = int(total_pos*(1-self.per_test))
        test_neg = int(total_neg*(1-self.per_test))

        poslinesTrain= pos[:train_pos]
        neglinesTrain= neg[:train_neg]
        poslinesTest= pos[test_pos:]
        neglinesTest= neg[test_neg:]

#        poslinesTrain= []
#        neglinesTrain= []
#        poslinesTest= []
#        neglinesTest= []
#
#        for _ in range(train_pos):
#            while(True):
#                rand = randint(0, train_pos)
#                if rand not in pos_rand_train:
#                    poslinesTrain.append(pos[rand])
#                    pos_rand_train.append(rand)
#                    break
#
#        for i in range(total_pos):
#            if i not in pos_rand_train:
#                poslinesTest.append(pos[i])
#
#
#        for _ in range(train_neg):
#            while(True):
#                rand = randint(0, train_neg)
#                if rand not in neg_rand_train:
#                    neglinesTrain.append(neg[rand])
#                    neg_rand_train.append(rand)
#                    break
#
#        for i in range(total_neg):
#            if i not in neg_rand_train:
#                neglinesTest.append(neg[i])

        train_pos = len(poslinesTrain)
        train_neg = len(neglinesTrain)
        test_pos = len(poslinesTest)
        test_neg = len(neglinesTest)

        train = open(self.training_file, "w")
        test = open(self.testing_file, "w")

# training set
        error = 0
        larger = train_pos if (train_pos > train_neg) else train_neg

        for i in range(larger):
            try:
                train.write(poslinesTrain[i])
                train.write("\n")
            except:
                error += 1
            try:
                train.write(neglinesTrain[i])
                train.write("\n")
            except:
                error += 1
# testing set
        larger = test_pos if (test_pos > test_neg) else test_neg


        for i in range(larger):
            try:
                test.write(poslinesTest[i])
                test.write("\n")
            except:
                error += 1
            try:
                test.write(neglinesTest[i])
                test.write("\n")
            except:
                error += 1
        print "total error occured : ", str(error)
        return