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
feature = [1,2,3,4]
d = {'col1': [1,2,3,4], 'col2': [1,2,3,4]}
df = pd.DataFrame(d )
NEW_DF = concat.concat_feature(feature,df)

# train_test_split
X, y = np.arange(10).reshape((5, 2)), range(5)
X_train, X_test, y_train, y_test = train_test_split.train_test(X, y)

X_train, X_val, y_train, y_val = train_test_split.train_val(X_train, y_train)
