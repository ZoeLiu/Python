from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    
    ''' 
    Use ggplot to make another data visualization focused on the MTA and weather
    data. Test on different plots
    
    '''
    ## 1. Ridership by time of day
    # aggregate entries to total level
    sum_entries = turnstile_weather[['Hour','ENTRIESn_hourly']].groupby(['Hour'],as_index=False).sum()

    plot1 =  ggplot(sum_entries, aes('Hour','ENTRIESn_hourly')) + \
            geom_point() + geom_line() + \
            scale_x_continuous(breaks=range(0,24,1),limits=(0,23)) + \
            scale_y_continuous(breaks=range(0,8000000,1000000),labels='comma') + ggtitle('Ridership by Hour of the Day') + xlab('Hour of the Day') + ylab('Total Subway Entries')   
            #scale_y_continuous(breaks=range(0,8000000,1000000), labels=["0K","100K","200K","300K","400K","500K","600K","700K","800K"]) 
    
    ## 2. How ridership varies by subway station
    # aggregate entries for each subway station
    subway = turnstile_weather[['UNIT','ENTRIESn_hourly']].groupby(['UNIT'],as_index=False).sum()
    #subway['nUNIT'] = subway.apply(lambda r: int(r['UNIT'].split('R')[1]), axis=1) 
    plot2 = ggplot(subway, aes('UNIT','ENTRIESn_hourly')) + geom_bar(stat = 'identity') 
    
    ## 3. Ridership by Station and Hour
    subway_by_hour = turnstile_weather[['UNIT','Hour','ENTRIESn_hourly']].groupby(['UNIT','Hour'], as_index=False).mean()
    plot3 = ggplot(subway_by_hour, aes('Hour', 'UNIT')) + geom_tile(fill='ENTRIESn_hourly')
    return plot1


if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(f, gg)
