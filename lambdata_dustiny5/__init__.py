#!/user/bin/env python
'''
lambdata - A collection of Data Science helper functions
'''

import pandas as pd
import numpy as np
from . import example_module
from . import train_test_split as tts
from . import concat

TEST = pd.DataFrame(np.ones(10))

# example_module
Y = example_module.increment(example_module.x)

# concat
#feature = [1,2,3,4]
#d = {'col1': [1,2,3,4], 'col2': [1,2,3,4]}

NEW_DF = concat.concat_feature(feature=None,df=None)

# train_test_split and train_val_split
#X, y = np.arange(10).reshape((5, 2)), range(5)

# Module returns X_train, X_test, y_train, y_test
TRAIN_TEST = tts.train_test(X=None, y=None)

# Module returns X_train, X-val, y_train, y_val
TRAIN_VAL = tts.train_val(X=None, y=None)
