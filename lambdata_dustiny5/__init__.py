#!/user/bin/env python
'''
lambdata - A collection of Data Science helper functions
'''

import pandas as pd
import numpy as np
from . import example_module
from . import explore_df
from . import train_test_split
from . import concat

TEST = pd.DataFrame(np.ones(10))

# example_module
Y = example_module.increment(example_module.x)

# concat
#feature = [1,2,3,4]
#d = {'col1': [1,2,3,4], 'col2': [1,2,3,4]}
feature = list()
df = pd.DataFrame()
NEW_DF = concat.concat_feature(feature,df)

# train_test_split and train_val_split
#X, y = np.arange(10).reshape((5, 2)), range(5)
X = pd.DataFrame()
y = pd.DataFrame()

# Module returns X_train, X_test, y_train, y_test
TRAIN_TEST = train_test_split.train_test(X, y)

# Module returns X_train, X-val, y_train, y_val
TRAIN_VAL = train_test_split.train_val(TRAIN_TEST[0], TRAIN_TEST[2])
