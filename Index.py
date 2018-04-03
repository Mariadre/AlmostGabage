
# coding: utf-8

# # Welcome to Jupyter!

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display


# In[3]:


from scipy import sparse

eye = np.eye(4)
print('Numpy array: \n{}'.format(eye))


# In[5]:


sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))


# In[8]:


data = np.ones(4)
# print(data)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print('COO representation:\n{}'.format(eye_coo))


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker='x')


# In[20]:


import pandas as pd
from IPython.display import display

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Location': ['NY', 'Paris', 'Berlin', 'London'],
        'Age': [24, 13, 53, 36]}
data_pandas = pd.DataFrame(data)
display(data_pandas)


# In[21]:


display(data_pandas[data_pandas.Age > 30])


# In[23]:


from sklearn.datasets import load_iris
iris_dataset = load_iris()

print('Keys of iris_dataset:\n{}'.format(iris_dataset.keys()))


# In[25]:


print(iris_dataset['DESCR'])


# In[27]:


print('Target Names:\n{}'.format(iris_dataset['target_names']))
print('Feature Names:\n{}'.format(iris_dataset['feature_names']))
print('Data:\n{}'.format(iris_dataset['data']))
print('Target:\n{}'.format(iris_dataset['target']))


# In[28]:


print('Type of Data:\n{}'.format(type(iris_dataset['data'])))
print('Type of Target:\n{}'.format(type(iris_dataset['target'])))


# In[30]:


print('Shape of target:\n{}'.format(iris_dataset['target'].shape))
print('Shape of data:\n{}'.format(iris_dataset['data'].shape))


# In[37]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
iris_dataset['data'], iris_dataset['target'], random_state=0)

print('X_train shape:\n{}'.format(X_train.shape))
print('y_train shape:\n{}'.format(y_train.shape))

print('X_test shape:\n{}'.format(X_test.shape))
print('y_test shape:\n{}'.format(y_test.shape))


# In[40]:


print(iris_dataset.feature_names)


# In[41]:


iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker="o", hist_kwds={'bins': 20}, s=60, alpha=.8)


# In[42]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)


# In[43]:


knn.fit(X_train, y_train)


# In[44]:


X_new = np.array([[5, 2.9, 1, 0.2]])
print('Shape of X_new:\n{}'.format(X_new.shape))


# In[45]:


prediction = knn.predict(X_new)

print('Prediction:\n{}'.format(prediction))
print('Predicted target name:\n{}'.format(iris_dataset['target_names'][prediction]))


# In[46]:


y_pred = knn.predict(X_test)
print('Test set predictions:\n{}'.format(y_pred))


# In[47]:


print('Test set score:\n{:.2f}'.format(knn.score(X_test, y_test)))

