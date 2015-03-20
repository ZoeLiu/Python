import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    ''' 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    plot two histograms on the same axes, showing hourly
    entries when raining vs. when not raining    '''
    
    plt.figure()
    # plot a historgram for hourly entries when it is raining
    turnstile_weather.loc[turnstile_weather['rain']==1]['ENTRIESn_hourly'].hist()
    # plot a historgram for hourly entries when it is not raining
    turnstile_weather.loc[turnstile_weather['rain']==0]['ENTRIESn_hourly'].hist()
    return plt


if __name__ == "__main__":
    image = "plot.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    plt = entries_histogram(turnstile_weather)
    plt.savefig(image)
