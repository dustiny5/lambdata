#!/user/bin/env/python
'''
Train test split a Data Frame
'''

from sklearn.model_selection import train_test_split
import pandas as pd

#X = pd.DataFrame()
#y = pd.Series()

def train_test(X, y):
    '''
    Features can be 1 or more dimension/column - X takes in a DataFrame
    Target 1 dimension/column - y takes in a Series
    Returns X_train, X_test, y_train, y_test
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_val(X, y):
    '''
    Features can be 1 or more dimension/column - X_train takes in a DataFrame
    Target 1 dimension/column - y_train takes in a Series
    Returns X_train, X_test, y_train, y_test
    '''
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_val, y_train, y_val