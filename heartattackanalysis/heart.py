#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sb
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


heart_data=pd.read_csv('heart.csv')


# In[3]:


heart_data.head()


# In[4]:


o2_data=pd.read_csv('o2Saturation.csv')


# In[5]:


o2_data.head()


# In[6]:


heart_data.info()


# As we can see that data is almost good and thus dosen't need anykind of preprocessing

# In[7]:


heart_data.describe()


# # EDD

# In[8]:


sb.scatterplot(x='age',y='output',data=heart_data)


# In[9]:


sb.boxplot(x='age',data=heart_data)


# In[10]:


sb.countplot(x='sex',data=heart_data)


# In[11]:


sb.countplot(x='output',data=heart_data)


# In[12]:


sb.countplot(x='fbs',data=heart_data)


# In[13]:


plt.figure(figsize=(18,15))
sb.heatmap(data=heart_data.corr())


# ### Making the data ready for training and testing

# In[14]:


from sklearn.model_selection import train_test_split


# In[15]:


X=heart_data.iloc[:,:13]
Y=heart_data.iloc[:,13]


# In[16]:


X_train,X_test,y_train,y_test=train_test_split(X,Y,random_state=42,test_size=0.2)


# # Logistic Regression

# In[17]:


from sklearn.linear_model import LogisticRegressionCV


# In[18]:


lrc=LogisticRegressionCV(Cs=20,cv=10,verbose=2)


# In[19]:


lrc.fit(X_train,y_train)


# In[20]:


y_pred=lrc.predict(X_test)


# #### Metrics for calculating error and accuracy of the model

# In[21]:


from sklearn.metrics import mean_absolute_error,mean_squared_error,accuracy_score


# In[22]:


print(mean_absolute_error(y_pred,y_test))
print(mean_squared_error(y_pred,y_test))
print(accuracy_score(y_test,y_pred))


# In[23]:


sb.displot(y_pred-y_test,kind='kde')


# # Standardrizing the data for Support Vector Machine

# ### Standarization is very importatant while using Support Vector Machine

# In[24]:


from sklearn.preprocessing import StandardScaler


# In[25]:


st=StandardScaler()


# In[26]:


st.fit(X_train)


# In[27]:


X_train_std=st.transform(X_train)


# In[28]:


X_test_std=st.transform(X_test)


# In[29]:


from sklearn import svm


# In[30]:


svm_cl=svm.SVC(kernel='linear',C=0.01)


# In[31]:


svm_cl.fit(X_train_std,y_train)


# In[32]:


y_pred=svm_cl.predict(X_test_std)


# In[33]:


from sklearn.metrics import accuracy_score,confusion_matrix


# In[34]:


confusion_matrix(y_test,y_pred)


# In[35]:


accuracy_score(y_test,y_pred)


# ##  Hyperparameter Tuning using Grid Search CV

# In[36]:


from sklearn.model_selection import GridSearchCV


# In[37]:


params={'C':(0.01,0.05,0.001,1,1.5,2,5,10,100,50,1000),'kernel':('poly','linear')}


# In[38]:


svc_g=svm.SVC(degree=3)


# In[39]:


svc_gs=GridSearchCV(svc_g,params,n_jobs=-1,cv=10,verbose=1,scoring='accuracy')


# In[40]:


svc_gs.fit(X_train_std,y_train)


# In[41]:


svc_gs.best_params_


# In[42]:


svcg=svc_gs.best_estimator_


# In[43]:


accuracy_score(y_test,svcg.predict(X_test_std))


# ## Validating the model using roc curve and auc

# In[44]:


from sklearn.metrics import roc_curve,auc


# In[45]:


log_fpr,log_tpr,log_thrs=roc_curve(y_test,lrc.decision_function(X_test))
auc_logistic=auc(log_fpr,log_tpr)


# In[46]:


svm_fpr,svm_tpr,thresh=roc_curve(y_test,svc_gs.decision_function(X_test))
auc_svc=auc(svm_fpr,svm_tpr)


# In[47]:


plt.figure(figsize=(10,10),dpi=100)
plt.plot(svm_fpr, svm_tpr, linestyle='-', label='SVM (auc = %0.3f)' % auc_svc)
plt.plot(log_fpr, log_tpr, marker='.', label='Logistic (auc = %0.3f)' % auc_logistic)

plt.xlabel('False Positive Rate -->')
plt.ylabel('True Positive Rate -->')

plt.legend()

plt.show()


# In[48]:


svc_gs.decision_function(X_test)


# ### Using another algorithm for mode XGBOOST

# In[49]:


import xgboost


# In[50]:


model_xg=xgboost.XGBClassifier(learning_rate=0.01,verbose=1,importance_type='total_gain')
model_xg.fit(X_train,y_train)


# In[51]:


y_xg=model_xg.predict(X_test)


# In[52]:


accuracy_score(y_test,y_xg)


# In[53]:


xg_fpr,xg_tpr,thresh=roc_curve(y_test,y_xg)


# In[54]:


auc_xg=auc(xg_fpr,xg_tpr)


# In[55]:


plt.figure(figsize=(10,10),dpi=100)
plt.plot(svm_fpr, svm_tpr, linestyle='-', label='SVM (auc = %0.3f)' % auc_svc)
plt.plot(log_fpr, log_tpr, marker='.', label='Logistic (auc = %0.3f)' % auc_logistic)
plt.plot(xg_fpr, xg_tpr, marker='.', label='Xgboost (auc = %0.3f)' % auc_xg)

plt.xlabel('False Positive Rate -->')
plt.ylabel('True Positive Rate -->')

plt.legend()

plt.show()


# #### As we can see that logistic regression performs much better than any of other two algorithms because the data is small and secondly the data is balanced and using complex algorithm may lead to overfitting

# In[ ]:




