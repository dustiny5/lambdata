#!/users/bin/env/python
'''
Input a list and change to a series. Finally concat to a new Data Frame
'''
import pandas as pd


def concat_feature(feature=None, df=None):
    '''
    Input a list and change to a series. Finally concat to a new Data Frame
    '''
    feature_series = pd.Series(feature)
    return pd.concat([df, feature_series], axis=1)

    
    
    

