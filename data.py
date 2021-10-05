# Program to create Dataframe of three series
import pandas as pd

# Define series 1
s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])

# Define series 2	
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])

# Define series 3
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])	

# Define Data
Data ={'first':s1, 'second':s2, 'third':s3}

# Create DataFrame
dfseries = pd.DataFrame(Data)			
