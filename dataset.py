import numpy as np
import re

class Dataset:
    def __init__(self, X, y):
        self._x = X # messages 
        self._y = y # tags ["spam", "ham"]
        self.train = None # tuple of (X_train, y_train)
        self.val = None # tuple of (X_val, y_val)
        self.test = None # tuple of (X_test, y_test)
        self.label2num = {} # dictionary used to convert labels to numbers
        self.num2label = {} # dictionary used to convert numbers to labels
        self._transform()
        
    def __len__(self):
        return len(self._x)
    
    def _transform(self):
        '''
        Function for clearing messages and converting labels to numbers
        '''
        unique = np.unique(self._y)
        for i in range(len(unique)):
            self.num2label[i] = unique[i]
            self.label2num[unique[i]] = i
        
        for i in range(len(self._y)):
            self._y[i] = self.label2num[self._y[i]]
        
        for i in range(len(self._x)):
            self._x[i] = re.sub("\W"," ",self._x[i])
            self._x[i] = " ".join(self._x[i].split())
            self._x[i] = self._x[i].lower().strip()
        pass

    def split_dataset(self, val=0.1, test=0.1):
        '''
        A function that splits dataset into train-validation-test sets
        '''
        np.random.seed(1)
        indices = np.arange(0,len(self))
        np.random.shuffle(indices)
        val_indices = indices[:round(val*len(self))]
        test_indices = indices[round(val*len(self)):round((val+test)*len(self))]
        train_indices = indices[round((val+test)*len(self)):]
        self.train = (self._x[train_indices], self._y[train_indices])
        self.val = (self._x[val_indices], self._y[val_indices])
        self.test = (self._x[test_indices], self._y[test_indices])
        pass
