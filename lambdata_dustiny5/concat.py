#!/users/bin/env/python
'''
Input a list and change to a series. Finally concat to a new Data Frame
'''
import pandas as pd

#feature = list()
#df = pd.DataFrame()

def concat_feature(feature, df):
    '''
    Input a list and change to a series. Finally concat to a new Data Frame
    Returns a pandas dataframe of concatenated column to the data frame
    '''
    feature_series = pd.Series(feature)
    df = pd.DataFrame(df)
    return pd.concat([df, feature_series], axis=1)