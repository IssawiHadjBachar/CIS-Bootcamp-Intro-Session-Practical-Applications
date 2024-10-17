import pandas as pd

# Assuming the file exists in the specified path
data = pd.read_csv('bitcoin_metrics.csv')

# Print the first 5 rows of the data
data.head()

data_processed =data.pivot_table(index='date', columns='code', values='value',aggfunc='first').reset_index()

data_processed.head()

data_processed.shape

# prompt: describe

import pandas as pd

data_processed.describe()

data_processed.columns

# prompt: data_processed , types

# Assuming data_processed is already defined as in your previous code

# Get the data types of each column
types = data_processed.dtypes

# Print the data types
print(types)

# List of deprecated column codes
deprecated_codes = ['BCDDC', 'BCDDE', 'BCDDM', 'BCDDW', 'BCDDY', 'NETDF', 'TVTVR']

# Drop the specified columns from the DataFrame and ignore errors if columns don't exist
data_processed = data_processed.drop(columns=deprecated_codes, errors='ignore')

# Print the first 5 rows of the processed DataFrame
data_processed.head()

# Convert the 'date' column to datetime format
data_processed['date'] = pd.to_datetime(data_processed['date'])

# Extract the day of the week (0 = Monday, 6 = Sunday)
data_processed['day_of_week'] = data_processed['date'].dt.dayofweek  # Monday=0, Sunday=6

# Extract the month as a number
data_processed['month'] = data_processed['date'].dt.month  # Month as a number

# Extract the year
data_processed['year'] = data_processed['date'].dt.year  # Year

data_processed.head()

# prompt: drop the date column

# Assuming data_processed is already defined as in your previous code

# Drop the 'date' column
data_processed = data_processed.drop(columns=['date'])

# Print the first 5 rows of the processed DataFrame
data_processed.head()

# prompt: how to see missing values

# Count the number of missing values in each column
missing_values = data_processed.isnull().sum()

# Print the missing values
print(missing_values)

# prompt: delete missing values

# Assuming data_processed is already defined as in your previous code

# Drop rows with any missing values
data_processed = data_processed.dropna()

# Print the first 5 rows of the processed DataFrame
data_processed.head()

# Count the number of missing values in each column
missing_values = data_processed.isnull().sum()

# Print the missing values
print(missing_values)

# prompt: normilize the data

from sklearn.preprocessing import MinMaxScaler

# Assuming data_processed is already defined as in your previous code

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Fit and transform the data
normalized_data = scaler.fit_transform(data_processed)

# Convert the normalized data back to a DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=data_processed.columns)

# Print the first 5 rows of the normalized DataFrame
normalized_df.head()