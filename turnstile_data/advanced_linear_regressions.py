import numpy as np
import pandas as pd
import scipy
import statsmodels

"""
This function takes in pandas 
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.  
"""

def predictions(weather_turnstile):
    dummy_units = pandas.get_dummies(weather_turnstile['UNIT'], prefix='unit')  
    features = weather_turnstile[['rain', 'precipi', 'Hour', 'meantempi']].join(dummy_units)
    values = weather_turnstile[['ENTRIESn_hourly']]                                              
    
    # add constant to the X
    features = sm.add_constant(features)
    
    # run OLS regression and store the results
    model = sm.OLS(values, features)
    results = model.fit()
    prediction = results.predict(features)
    return prediction

def compute_r_squared(data, predictions):
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-np.mean(data))**2).sum()
    r_squared = SSReg / SST

    return r_squared

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values) 

    print r_squared
