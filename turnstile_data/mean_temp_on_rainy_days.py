import pandas as pd
import pandasql

def min_temperature_on_rainy_days(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data. Find the average
    minimum temperature on rainy days where the minimum temperature
    is greater than 55 degrees.
    
    '''
    weather_data = pd.read_csv(filename)

   q = """
    select avg(cast (mintempi as integer))
    from weather_data
    where rain = 1 and mintempi > 55
    """
    
    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends


if __name__ == "__main__":
    input_filename = "weather_underground.csv"
    output_filename = "output.csv"
    student_df = min_temperature_on_rainy_days(input_filename)
    student_df.to_csv(output_filename)
