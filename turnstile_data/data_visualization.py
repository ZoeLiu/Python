from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data.
    Test on different types of plot
    
    '''
    ## 0. Exploration: Histogram of entries in rain day vs non-rain days
    plot0 = turnstile_weather['ENTRIESn_hourly'].hist(by=turnstile_weather['rain'])
    
    
    ## 1. Ridership by time of day
    plot1 = ggplot(turnstile_weather,aes('Hour','ENTRIESn_hourly')) + \
            geom_point(color='black') + geom_line(color='black') + \
            ggtitle('Ridership by Hour of the Day') + xlab('Hour of the Day') + ylab('Subway Entries')
    ## 2. Ridership by Subway station
   
    #turnstile_weather['DATEn'] = pandas.to_datetime(turnstile_weather['DATEn'])
    subway = turnstile_weather[['UNIT','ENTRIESn_hourly']].groupby(['UNIT'],as_index=False).mean()    
    subway['nUNIT'] = subway.apply(lambda r: int(r['UNIT'].split('R')[1]), axis=1) 
    
    plot2 = ggplot(subway,aes('nUNIT','ENTRIESn_hourly')) + \
            geom_point(color='blue')  + \
            ggtitle('Ridership in May 2011 by Subway Station') + xlab('Subway Station') + ylab('Subway Entries')
    
    ## 3. Which stations have more entries at different times of day
    #create data that summarize the entries by subway and hour
    subway_by_hour = turnstile_weather[['UNIT','Hour','ENTRIESn_hourly']].groupby(['UNIT','Hour'], as_index=False).mean()
    subway_by_hour['nUNIT'] = subway_by_hour.apply(lambda r: int(r['UNIT'].split('R')[1]), axis=1) 
    #create bubble plot
    plot3 = plt.scatter(subway_by_hour['Hour'],subway_by_hour['nUNIT'],s=subway_by_hour['ENTRIESn_hourly'])

    return plot0

if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(f, gg)
