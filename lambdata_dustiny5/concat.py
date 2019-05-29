#!/user/bin/env/python
'''
Input a list and change to a series. Finally concat to a new Data Frame
'''
import pandas as pd

class ConcatFeature:
    '''
    -Input a list and change to a series. Finally concat to a new Data Frame
    -Returns a pandas dataframe of concatenated column to the data frame
    '''
    # feature are columns of data frame and df is panda's data frame
    def __init__(self, feature, df):
        self.feature = feature
        self.df = df
    
    def concat(self):

        # Change list to a Series
        feature_series = pd.Series(self.feature)

        # Input a dictionary Change to dataframe
        df = pd.DataFrame(self.df)

        # Return new datafram with concatenated feature
        return pd.concat([df, feature_series], axis=1)



################## Old Code ##################
#feature = list()
#df = pd.DataFrame()

# def concat_feature(feature, df):
#     '''
#     Input a list and change to a series. Finally concat to a new Data Frame
#     Returns a pandas dataframe of concatenated column to the data frame
#     '''
#     feature_series = pd.Series(feature)
#     df = pd.DataFrame(df)
#     return pd.concat([df, feature_series], axis=1)