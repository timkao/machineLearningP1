
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



