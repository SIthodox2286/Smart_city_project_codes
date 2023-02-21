#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from load_data import load_categorical_data
from load_data import load_categorical_more_data
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor



"""
Use Decision Tree to fit the relationship between 
homeless_real_value and other variables, except 
no_longer_homeless, prevention_duty, and relief duty.
"""

#Read data
categorical_data,local_authority_names,total_duty_owed,total_population_in_households,prevention_duty_owed,relief_duty_owed,support_need_homeless,no_longer_homeless,homeless_real_value,categorical_waiting_list_size,social_housing_lettings_2021,band_A_B_properties,band_C_D_properties,band_E_F_properties,band_G_H_properties,median_prices,median_earning_gross,categorical_median_afforability_ratio,lower_quatile_prices,lower_quatile_earning_gross,categorical_lower_quatile_afforability_ratio = load_categorical_data()

affordableRent_start,social_housing_start,intermediate_start,total_affordable_start,affordable_complete,social_complete,intermediate_complete,total_affordable_complete=load_categorical_more_data()


# Generate X and Y:
X = pd.DataFrame([total_duty_owed,\
                  total_population_in_households,\
                  support_need_homeless,\
                  categorical_waiting_list_size,\
                  social_housing_lettings_2021,band_A_B_properties,\
                  band_C_D_properties,band_E_F_properties,band_G_H_properties,\
                  median_prices,median_earning_gross,categorical_median_afforability_ratio,\
                  lower_quatile_prices,lower_quatile_earning_gross,\
                  categorical_lower_quatile_afforability_ratio,\
                  affordableRent_start,social_housing_start,\
                  intermediate_start,total_affordable_start,\
                  affordable_complete,social_complete,intermediate_complete,\
                  total_affordable_complete])
X = X.transpose()
Y=homeless_real_value


#Split train and test data, their ratio is 7 to 3:
train_X,test_X,train_Y,test_Y = train_test_split(X,Y, test_size=0.3, random_state=0)


#Fit a Decision Tree
regr = DecisionTreeRegressor(max_depth=3)
regr=regr.fit(train_X, train_Y)

# #Plot the tree
# plt.figure(dpi=1600)
# tree.plot_tree(regr,feature_names=list(test_X),fontsize=3) 
# plt.savefig('Figure/Decision_Tree.png')


#Predict on the test data
predict_Y = regr.predict(test_X)

#Plot and save the test results
f_predictions = predict_Y
test_y = test_Y

N =len(f_predictions)
locations = range(1,N+1)

# Position of bars on x-axis
y_pos = np.arange(N)

# Width of a bar 
width = 0.3

# Plotting
plt.rcParams.update({'font.size': 15})
fig_r2, ax = plt.subplots(figsize=(16,8))
plt.bar(y_pos, f_predictions, width, label='Predictions')
plt.bar(y_pos + width, test_y, width, label='Data')
plt.xlabel('Locations')
plt.ylabel('Homeless Value')
plt.title('Multi Variables Decision Tree Regression Predictions on Homeless Value')

# xticks()
plt.xticks(y_pos + width / 2, list(local_authority_names[test_y.index]))
plt.setp(ax.get_xticklabels(), fontsize=12, rotation='vertical')

# Size of the Plot
plt.xlim([-2,max(y_pos)+2])

# Finding the best position for legends and putting it
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('Figure/Decision_Tree_test_result.png')
plt.show()

