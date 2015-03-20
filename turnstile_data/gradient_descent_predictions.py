import pandas as pd
import numpy as np

def normalize_features(array):
   """
   Normalize the features in our data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and the values for our thetas.
    
    """
    
    m = len(values)
    predicted_values = np.dot(features,theta)
    sum_of_square_errors = np.square(predicted_values - values).sum()
    cost = sum_of_square_errors /(2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.

    """
    m = len(values)
    cost_history = []


    for i in range(num_iterations):
        predicted_values = np.dot(features, theta)
        theta = theta + alpha/m*np.dot((values-predicted_values),features) 
        cost = compute_cost(features,values,theta)
        cost_history.append(cost)
        
    return theta, pd.Series(cost_history)

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pd dataframe called weather_turnstile.
    Using the information stored in the dataframe, predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    '''
    # create dummy variables for UNIT 
    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    
    
    # Select Features and add dummy UNIT to the dataframe
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']].join(dummy_units)

    # Values
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)

    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    # Set values for alpha, number of iterations.
    alpha = 0.1 
    num_iterations = 75 

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
                                                            alpha, num_iterations)
    predictions = np.dot(features_array, theta_gradient_descent)
    # call plot
    plot = plot_cost_history(alpha, cost_history) 
    return predictions, plot

def compute_r_squared(data, predictions):
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-np.mean(data))**2).sum()
    r_squared = SSReg / SST

    return r_squared


def plot_cost_history(alpha, cost_history):
   """This function is for viewing the plot of cost history.
   """
   cost_df = pandas.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
      geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )



if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values) 

    print r_squared
