import pandas as pd
import pandasql

def avg_min_temperature(filename):
    '''
    This function run a SQL query on a dataframe of
    weather data.  The SQL query return one column and
    one row - the average meantempi on days that are a Saturday
    or Sunday (i.e., the the average mean temperature on weekends).
    '''
    weather_data = pd.read_csv(filename)

    q = """
    select avg(cast (meantempi as integer))
    from weather_data
    where cast (strftime('%w', date) as integer) = 0 or cast (strftime('%w', date) as integer) = 6
    """
    
    #Execute SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends

if __name__ == "__main__":
    input_filename = "weather_underground.csv"
    output_filename = "output.csv"
    student_df = avg_min_temperature(input_filename)
    student_df.to_csv(output_filename)
