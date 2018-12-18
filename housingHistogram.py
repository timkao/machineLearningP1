
#%%
import os
import tarfile
import pandas as pd
from six.moves import urllib
from utils.fetchData import load_housing_data

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("dataset", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

housing = load_housing_data(HOUSING_PATH)
housing.head()


#%%
housing.head()


#%%
housing2 = load_housing_data()


#%%
housing2.head()


#%%
housing.info()


#%%
housing["ocean_proximity"].value_counts()


#%%
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20, 15))
plt.show()


#%%
import numpy as np


#%%
import os
import tarfile
import pandas as pd
from six.moves import urllib
from utils.fetchData import load_housing_data

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("dataset", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

housing = load_housing_data(HOUSING_PATH)


housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
housing["income_cat"].hist()


#%%
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_idx, test_idx in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_idx]
    strat_test_set = housing.loc[test_idx]

strat_test_set["income_cat"].value_counts() / len(strat_test_set)


#%%
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)


#%%



