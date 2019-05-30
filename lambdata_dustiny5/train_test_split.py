#!/user/bin/env/python
'''
Train test split a Data Frame
'''
from sklearn.model_selection import train_test_split

class TrainTestSplit:
    '''
    Library:
    ------------------------------------
    from sklearn.model_selection import train_test_split

    Parameters:
    -------------------------------------
    feature - Takes in 1 or more dimension/column - X takes in a DataFrame
    target - Takes in 1 dimension/column - y takes in a Series
    test_size - Default is 20% or 0.2
    random_state - Default is 42

    Returns:
    --------------------------------------
    X_train, X_test, y_train, y_test
    '''
    
    def __init__(self, feature, target, test_size=0.2, random_state=42):
        self.feature = feature
        self.target = target
        self.test_size = test_size
        self.random_state = random_state

    def split(self):
        # Split to train and test data sets
        X_train, X_test, y_train, y_test = train_test_split(self.feature, self.target,     test_size=self.test_size, random_state=self.random_state)

        # Return X_train, X_test, y_train, y_test
        return X_train, X_test, y_train, y_test


##################  Old Code  ##############################

#X = pd.DataFrame()
#y = pd.Series()

# def train_test(feature, target, test_size=0.2):
#     '''
#     Features(X) can be 1 or more dimension/column - X takes in a DataFrame
#     Target(y) 1 dimension/column - y takes in a Series
#     Returns X_train, X_test, y_train, y_test
#     '''
#     X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=test_size, random_state=42)
#     return X_train, X_test, y_train, y_test
# def train_val(feature, target):
#     '''
#     Features(X) can be 1 or more dimension/column - X_train takes in a DataFrame
#     Target(y) 1 dimension/column - y_train takes in a Series
#     Returns X_train, X_test, y_train, y_test
#     '''
#     X_train, X_val, y_train, y_val = train_test_split(feature, target, test_size=0.2, random_state=42)
#     return X_train, X_val, y_train, y_val