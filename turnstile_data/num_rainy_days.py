import pandas as pd
import pandasql

def max_temp_aggregate_by_fog(filename):
    '''
    This function run a SQL query on a dataframe of
    weather data.  The SQL query return one column and
    one row - a count of the number of days in the dataframe where
    the rain column is equal to 1 (i.e., the number of days it
    rained). 
    '''
    weather_data = pd.read_csv(filename)

    q = """
    select count(*) 
    from weather_data
    where rain = 1
    
    """
    
    #Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days



if __name__ == "__main__":
    input_filename = "weather_underground.csv"
    output_filename = "output.csv"
    student_df = max_temp_aggregate_by_fog(input_filename)
    student_df.to_csv(output_filename)
