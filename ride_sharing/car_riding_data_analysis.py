
# coding: utf-8

# In[ ]:

'''
read json file and convert it to csv file
'''
import os
import json
import csv

os.chdir('/Users/ZoeL/workspace/')

with open('ride_sharing.json') as data_file:
    data = json.load(data_file)


f = csv.writer(open('ride_sharing.csv','wb+'))
f.writerow(["city", "trips_in_first_30_days", "signup_date", "avg_rating_of_driver", "avg_surge","last_trip_date","phone","surge_pct","black_user","weekday_pct","avg_dist","avg_rating_by_driver"])


for x in data:
    f.writerow([x["city"],
               x["trips_in_first_30_days"],
               x["signup_date"],
               x["avg_rating_of_driver"],
               x["avg_surge"],
               x["last_trip_date"],
               x["phone"],
               x["surge_pct"],
               x["black_user"],
               x["weekday_pct"],
               x["avg_dist"],
               x["avg_rating_by_driver"]])


# In[1]:

import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
import scipy
from scipy import stats
from pandas.tseries.offsets import *

ride = pd.read_csv("/Users/ZoeL/workspace/ride_sharing.csv")

''' 
data checking and cleaning 
'''
ride.dtypes
ride.head(10)
ride.describe()
# note: there are several variables have missing data. They seem to be un-rated scores by users. Will leave them as they are now

# create a boolean type of black_user (currently it is an object)
#ride['black_user'].astype(bool)
ride['n_black_user'] = ride['black_user'] == True
ride.dtypes


''' 
create retention flag 
'''
# find the the latest day of the last_trip_date, which we will assume is the day that the data was pulled
last_day = max(ride['last_trip_date']) 
print last_day  # 2014-07-01

# create a retention flag indicating if a user is retained (active in preceding 30 days)
ride['retention'] = (ride['last_trip_date'] > '2014-06-01').astype(int)
#print np.mean(ride['retention'])


#print ride['retention'].head(10)
#print ride['last_trip_date'].head(10)
#ride.loc[ride['retention']==1]['avg_rating_of_driver'].hist()
#ride.loc[ride['retention']==0]['avg_rating_of_driver'].hist()



''' 
explorative analysis 
'''
# retention by month
 # create retention flag for each month
ride['retention_May'] = (ride['last_trip_date'] > '2014-05-01').astype(int) 
ride['retention_April'] = (ride['last_trip_date'] > '2014-04-01').astype(int)  
ride['retention_March'] = (ride['last_trip_date'] > '2014-03-01').astype(int)
ride['retention_Feburary'] = (ride['last_trip_date'] > '2014-02-01').astype(int)

all_retention = ride.ix[:,['retention_Feburary','retention_March','retention_April','retention_May','retention']].apply(np.mean)
print all_retention

'''
import math
x = [2,3,4,5,6]
low = 0
high = 0.5
plt.ylim([math.ceil(low-0.5*(high-low)), math.ceil(high+0.5*(high-low))])
plt.bar(x,all_retention) 
plt.title('Retention Rate by Month')
plt.xlabel('Month in 2014')
plt.show()
'''

# retention by city
 # check city counts
ride['city'].value_counts().sort_index()
# calculate the average retention rate by city
citygroup = ride['retention'].groupby(ride['city'])
avg_city_retention = citygroup.mean()
print avg_city_retention
#avg_city_retention.plot(kind='bar')
  
# retention by black_user
ubgroup = ride['retention'].groupby(ride['black_user'])
avg_ub_retention = ubgroup.mean()

ubgroup2 = ride['retention_May'].groupby(ride['black_user'])
avg_ub_retention2 = ubgroup2.mean()

ubgroup3 = ride['retention_April'].groupby(ride['black_user'])
avg_ub_retention3 = ubgroup3.mean()

ubgroup4 = ride['retention_March'].groupby(ride['black_user'])
avg_ub_retention4 = ubgroup4.mean()

ubgroup5 = ride['retention_Feburary'].groupby(ride['black_user'])
avg_ub_retention5 = ubgroup5.mean()

print avg_ub_retention, avg_ub_retention2,avg_ub_retention3,avg_ub_retention4,avg_ub_retention5

# metrics averages by retention
rtgroup = ride.groupby(ride['retention'])
avg_rt_retention = rtgroup.mean()
print avg_rt_retention



# use correlations to check which metrics are highly correlated with retention
print(ride.corr())
# note: retention is highly correlated with trips_in_first_30_days and black_user. second highest correlation with avg_dis. trips_in_first_30_days/
# is negatively correlated with trips_in_first_30_days. It looks like that the highest retention happens more in people who takes
# frequent short distance trips and those who have take ride for their first 30 days

### statistical testing

  # Mann-Whitney U Test to compare average trips_in_first_30_days by retention (since # of trips is not a normal distribution so we don't use t-test here)
  # data for retained and churned
    
# trips_in_first_30_days
retain_trip = ride.loc[ride['retention']==True]['trips_in_first_30_days']
churn_trip = ride.loc[ride['retention']==False]['trips_in_first_30_days']
  
retain_mean = np.mean(retain_trip)
churn_mean= np.mean(churn_trip)
   
U,p = scipy.stats.mannwhitneyu(retain_trip,churn_trip)
print retain_mean, churn_mean, U,p   

# black_user
retain_ub = ride.loc[ride['retention']==True]['n_black_user']
churn_ub = ride.loc[ride['retention']==False]['n_black_user']
  
retain_mean = np.mean(retain_ub)
churn_mean= np.mean(churn_ub)
   
U,p = scipy.stats.mannwhitneyu(retain_ub,churn_ub)
print retain_mean, churn_mean, U,p   

# average distance
retain_dist = ride.loc[ride['retention']==True]['avg_dist']
churn_dist = ride.loc[ride['retention']==False]['avg_dist']
  
retain_mean = np.mean(retain_dist)
churn_mean= np.mean(churn_dist)
   
U,p = scipy.stats.mannwhitneyu(retain_dist,churn_dist)
print retain_mean, churn_mean, U,p 

# weekday_pct
retain_pct = ride.loc[ride['retention']==True]['weekday_pct']
churn_pct = ride.loc[ride['retention']==False]['weekday_pct']
  
retain_mean = np.mean(retain)
churn_mean= np.mean(churn)

U,p = scipy.stats.mannwhitneyu(retain_pct,churn_pct)
print retain_mean, churn_mean, U,p 


# In[63]:

'''
Graphs
'''
# User retention by city

import plotly.plotly as py
from plotly.graph_objs import *

trace1 = Bar(
    x=["Astapor", "King's Landing", 'Winterfell','Total'],
    y=[24, 62, 34, 37],
    name='Retained User %'
)
trace2 = Bar(
    x=["Astapor", "King's Landing", 'Winterfell','Total'],
    y=[76, 38, 66, 63],
    name='Churned User %'
)
data = Data([trace1, trace2])
layout = Layout(
    barmode='stack'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='stacked-bar')
 


# In[64]:

# User retention by months for Black and Non Black users
trace1 = Bar(
    x=['Feburary','March','April','May','June'],
    y=[83.8682,77.1153,69.6196,61.7686,49.6419],
    name='rideBlack Users',
    marker=Marker(
        color='rgb(55, 83, 109)'
    )
)
trace2 = Bar(
    x=['Feburary','March','April','May','June'],
    y=[75.6545,66.8112,57.0428,46.799,28.7431],
    name='Non Black Users',
    marker=Marker(
        color='rgb(26, 118, 255)'
    )
)
data = Data([trace1, trace2])
layout = Layout(
    title='Retention Rate by Month - Black Users vs Non Users',
    xaxis=XAxis(
        tickfont=Font(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=YAxis(
        title='%',
        titlefont=Font(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=Font(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=Legend(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='style-bar')



# In[55]:

# Trips in first 30 days & avg_dist (retained vs churned)
trace0 = Bar(
    x=['Churned', 'Retained', 'Total'],
    y=[1.659437, 3.350104, 2.2786],
    marker=Marker(
        color=['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)', 'rgba(204,204,204,1)'],
    ),
)
data = Data([trace0])
layout = Layout(
    title='Average number of trips in first 30 days',
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='color-bar')


# In[5]:

# Correlation matrix plot
import seaborn as sns

sns.set(style="white")

ride['city_KL'] = (ride['city'] == "King's Landing").astype(int)
ride['city_A'] = (ride['city'] == "Astapor").astype(int)
ride['city_W'] = (ride['city'] == "Winterfell").astype(int)
#print ride['city'], ride['city_KL'],ride['city_A'],ride['city_W']

ride_corr = ride[['retention','city_A','city_KL','city_W','avg_dist','avg_rating_by_driver','avg_rating_of_driver','surge_pct','avg_surge',
                  'trips_in_first_30_days','n_black_user','weekday_pct']]
corr =ride_corr.corr()
print corr

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
            square=True, xticklabels=(" "," "," "," ","avg_dist"), yticklabels=("retention","city_Astapor","city_King's Landing"," ","avg_dist"," "," "," "," ","trips_in_first_30_days","black_user"," "),
            linewidths=0.5, cbar_kws={"shrink": .5}, ax=ax)
            


# In[81]:

'''
Predictive Modeling: predict user retention
'''


# In[34]:

col_names = ride.columns.tolist()
print col_names

y = ride['retention']
features = ride[['city_KL','city_A','trips_in_first_30_days','avg_rating_of_driver', 'avg_surge', 'surge_pct', 'n_black_user', 
                 'weekday_pct', 'avg_dist', 'avg_rating_by_driver']]

X0 = features.as_matrix().astype(np.float)

#Imputation for missing data
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(X0)
X = imp.transform(X0)

# Standardize scores
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#X = scaler.fit_transform(X)


# In[61]:

from sklearn.preprocessing import Imputer
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc

def run_cv(X,y,clf_class,**kwargs):
    # Construct a kfolds object
    kf = KFold(len(y),n_folds=10,shuffle=True)
    y_pred = y.copy()
    y_prob = y.copy()
    
    # Iterate through folds
    for train_index, test_index in kf:
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        # Initialize a classifier with key word arguments
        clf = clf_class(**kwargs)
        clf.fit(X_train,y_train)
        y_pred[test_index] = clf.predict(X_test)       
        y_prob[test_index] = clf.predict_proba(X_test)
        
        
    return y_pred, y_prob

from sklearn.linear_model import LogisticRegression as LR
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.ensemble import GradientBoostingClassifier as GB

def accuracy(y_true,y_pred,y_prob):
    
    # compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Compute ROC curve and area the curve
    fpr, tpr, thresholds = roc_curve(y_true, y_prob)
    roc_auc = auc(fpr, tpr)
    
    return np.mean(y_true == y_pred), cm, fpr, tpr, roc_auc

#print "Logistic Regression:"
#res_cv = run_cv(X,y,LR);
#results = accuracy(y, res_cv[0],res_cv[1]);
#print "%.4f" % results[0]
#print results[1]
#print results[4]
#print "Support vector machines:"
#print "%.3f" % accuracy(y, run_cv(X,y,SVC))
print "Random forest:"
res_cv = run_cv(X,y,RF);
results = accuracy(y, res_cv[0],res_cv[1]);
print "%.4f" % results[0]
print results[1],results[4]


#print "K-nearest-neighbors:"
#print "%.3f" % accuracy(y, run_cv(X,y,KNN))
#print "Gradient Boosting:"
#print "%.3f" % accuracy(y, run_cv(X,y,GB))

'''
# Plot ROC curve
import pylab as pl
pl.clf()
pl.plot(results[2], results[3], label='ROC curve (area = %0.2f)' % results[4])
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic example')
pl.legend(loc="lower right")
pl.show()


# In[ ]:



