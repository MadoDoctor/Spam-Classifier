import numpy as np
import re

class Model:
    def __init__(self, alpha=1):
        self.vocab = {} # a dictionary containing all the unique words from the train set
        self.spam = {} # a dictionary containing the frequency of words in spam messages from the train dataset
        self.ham = {} # a dictionary containing the frequency of words in non-spam messages from the train dataset
        self.alpha = alpha # smoothing
        self.label2num = {'ham':0, 'spam':1} # dictionary used to convert labels to numbers
        self.num2label = {0:'ham', 1:'spam'} # dictionary used to convert numbers to labels
        self.Nvoc = None # the total number of unique words in the train dataset
        self.Nspam = None # the total number of unique words in spam messages in the train dataset
        self.Nham = None # the total number of unique words in non-spam messages in the train dataset
        self._train_X, self._train_y = None, None
        self._val_X, self._val_y = None, None
        self._test_X, self._test_y = None, None

    def fit(self, dataset):
        '''
        dataset - an object of the Dataset class
        The function uses the input argument "dataset",
        to fill in all the attributes of a given class.
        '''
        self._train_X = dataset.train[0]
        self._train_y = dataset.train[1]
        self._val_X = dataset.val[0]
        self._val_y = dataset.val[1]
        self._test_X = dataset.test[0]
        self._test_y = dataset.test[1]
        
        for i in range(len(self._train_X)):
            self._train_X[i].split(" ")
        for i in self._train_X:
            for elem in i.split():
                if elem not in  self.vocab:
                    self.vocab[elem]=1
                else:
                    self.vocab[elem]+=1
        
        for i in range(len(self._train_X)):
            if self._train_y[i]==0:
                for elem in self._train_X[i].split():
                    if elem not in self.ham:
                        self.ham[elem]=1
                    else:
                        self.ham[elem]+=1
            else:
                for elem in self._train_X[i].split():
                    if elem not in self.spam:
                        self.spam[elem]=1
                    else:
                        self.spam[elem]+=1
                        
        self.Nvoc = len(self.vocab)
        self.Nspam = len(self.spam)
        self.Nham = len(self.ham)
    
    def inference(self, message):
        '''
        The function takes one message and, using a naive bayes classifier, detects it as spam / ham
        '''
        
        message= re.sub("\W"," ",message)
        message = " ".join(message.split())
        message = message.lower().strip()
        message = message.split()
        
        pspam = sum(self._train_y==1)/len(self._train_y)
        pham = sum(self._train_y==0)/len(self._train_y)
        
        for word in message:
            values = 0
            if word in self.spam:
                values = self.spam[word]
            pspam *= (values+self.alpha)/(sum(self.spam.values())+self.alpha*self.Nvoc)
            
        for word in message:
            values = 0
            if word in self.ham:
                values = self.ham[word]
            pham *= (values+self.alpha)/(sum(self.ham.values())+self.alpha*self.Nvoc)
            
        if pspam > pham:
            return "spam"
        return "ham"
    
    def validation(self):
        '''
        The function predicts the message labels from the validation dataset,
        and returns the prediction accuracy of message labels
        '''
        
        corrects = 0
        for i in range(len(self._val_X)):
            if self.inference(self._val_X[i]) == self.num2label[self._val_y[i]]:
                corrects+=1
        val_acc = corrects/len(self._val_y)
        
        return val_acc 

    def test(self):
        '''
        The function predicts message labels from the test dataset,
        and returns the prediction accuracy of message labels
        '''
        
        corrects = 0
        for i in range(len(self._test_X)):
            if self.inference(self._test_X[i]) == self.num2label[self._test_y[i]]:
                corrects+=1
        test_acc = corrects/len(self._test_y)
        
        return test_acc


