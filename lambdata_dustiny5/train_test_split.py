#!/user/bin/env/python
'''
Train test split a Data Frame
'''

from sklearn.model_selection import train_test_split


def train_test(X=None, y=None):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_val(X=None, y=None):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_val, y_train, y_val