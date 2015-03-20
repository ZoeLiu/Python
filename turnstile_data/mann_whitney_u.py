import numpy as np
import scipy
import scipy.stats
import pd


def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe.This 
    function return the mean number of entries with rain, the mean number of entries without rain, and the
    Mann-Whitney U statistic and p-value.
    '''

    # create data for rain and no rain 
    rain = turnstile_weather.loc[turnstile_weather['rain']==1]['ENTRIESn_hourly']
    no_rain = turnstile_weather.loc[turnstile_weather['rain']==0]['ENTRIESn_hourly']
    
    # calculate the mean of entries for rain days and no rain days
    with_rain_mean = np.mean(rain)
    without_rain_mean = np.mean(no_rain)
    
    # Mann-Whitney Test
    U,p = scipy.stats.mannwhitneyu(rain,no_rain)

    return with_rain_mean, without_rain_mean, U, p

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_output = mann_whitney_plus_means(turnstile_master)

    print student_output
