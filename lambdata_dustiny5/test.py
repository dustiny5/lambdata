import unittest
import pandas as pd
from train_test_split import TrainTestSplit
from concat import ConcatFeature


class LambdataTestConcat(unittest.TestCase):
    '''
    Test the Modules
    '''
    # Dummy feature and dictionary for testing
    feature = [i for i in range(1,11)]
    my_dict = {'col1': [i for i in range(1,11)], 'col2': [i for i in range(1,11)]}

    def test_concat(self, feature=feature, my_dict=my_dict):
        merge = ConcatFeature(feature, my_dict)
        df = merge.concat()
        self.assertEqual(type(df), type(pd.DataFrame()))



if __name__ == '__main__':
    unittest.main()