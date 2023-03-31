#import requests
#import json

# Replace YOUR_API_KEY with your actual API key
#api_key = 'AIzaSyDTw9NFOiPRmd3ACwowhSfKVXUYXhBOeiU'

# Define a list of origin and destination pairs
#origins = ['Seattle', 'Los Angeles', 'Chicago']
#destinations = ['San Francisco', 'New York', 'Miami']

#for origin in origins:
 #   for destination in destinations:
  #      url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + origin + '&destinations=' + destination + '&key=' + api_key
   #     response = requests.get(url)
    #    data = response.json()
     #   traffic = data['rows'][0]['elements'][0]['duration_in_traffic']['text']
      #  print("The traffic from", origin, "to", destination, "is", traffic)
      
import googlemaps
import datetime

import itertools
import pandas as pd

# Import a CSV file
#df_csv = pd.read_csv('C://Users//oktina//Documents//ArcGIS//Projects//Placemaking_Pesisir_Utara//1_Access_Linkages//1_Point_Intersections_Road_v3.csv')

# Import an Excel file
df_excel = pd.read_excel('C://Users//oktina//Documents//ArcGIS//Projects//Placemaking_Pesisir_Utara//1_Access_Linkages//1_Point_Intersections_Road_v3.xlsx')

# Import a table from a SQL database
#import sqlite3
#conn = sqlite3.connect('mydatabase.db')
#df_sql = pd.read_sql('SELECT * FROM mytable', conn)
# Read the CSV file into a DataFrame
#df = pd.read_csv('mydata.csv')
df_excel['Lat'] = df_excel['Lat'].astype(str)
df_excel['Lat']
df_excel['Long'] = df_excel['Long'].astype(str)
df_excel['Long']
# Merge the values in column1 and column2 with a comma separator
df_excel['merged'] = df_excel['Lat'] + ',' + df_excel['Long']
df_excel['merged']
# Write the DataFrame back to a CSV file
#df.to_csv('mydata_with_merged_column.csv', index=False)
    
df_excel_test = df_excel['merged']
df_excel_test
# Replace with your API key
gmaps = googlemaps.Client(key='')

# Specify the start and end points of the route
#origins = ['-6.108484, 106.802252', '-6.108605, 106.801106', '-6.108142, 106.804386']
#destinations = ['-6.106714, 106.801932', '-6.108605, 106.801106', '-6.108484, 106.802252']
origins = df_excel_test
destinations = df_excel_test

# Define a matrix
#matrix = [['Seattle', 'Los Angeles', 'Chicago'],
#          ['San Francisco', 'New York', 'Miami']]

# Flatten the matrix into a list
#flat_list = [item for sublist in matrix for item in sublist]

# Generate all possible 2-object combinations
combinations = list(itertools.permutations(df_excel_test, 2))
combinations
# Print the combinations
#for combination in combinations:
#   print(combination)




# Get the directions and traffic data for the route
import numpy as np

# set the dimensions of the matrix
#rows = 
#cols = 1

# create an empty list to store the values
matrix_values = np.zeros((16000, 4), dtype=object)

i=0                            
# Print the duration and distance of the route, as well as the current traffic conditions
for origin in origins:
    for destination in destinations:
        try:
        # do something with value
            # Specify the departure time (optional)
            departure_time = datetime.datetime.now()
            directions_result = gmaps.directions(origin,
                                             destination,
                                             mode="driving",
                                             departure_time=departure_time,
                                             traffic_model="best_guess")
            route = directions_result[0]['legs'][0]
            #print("Route from ", origin, ", to ", destination)
            print("Route duration: {} minutes".format(route['duration']['text']))
            print("Route distance: {} miles".format(route['distance']['text']))
            print("Traffic: {}".format(route['duration_in_traffic']['text']))
            i=i+1
            matrix_values[i, 0] = route['duration_in_traffic']
            matrix_values[i, 1] = ["Route from ", origin, ", to ", destination]
            matrix_values[i, 2] = ["Route duration: {} minutes".format(route['duration']['text'])]
            matrix_values[i, 3] = ["Route distance: {} miles".format(route['distance']['text'])]
            #for i, value in enumerate(destination):
            #    # print the counter and the current value
            #    print(f"Loop {i+1}: {value}")
            # set the length of the vector
            #n = 5
            
            # create an empty 2D NumPy array with 1 column and n rows
            #matrix = np.zeros((n, 1), dtype=str)
            
            # generate values for the first column using a for loop
            #for i in range(n):
                # calculate the value for the i-th row of the first column
            #    value = i**2
                # assign the value to the i-th row of the first column
            #    matrix[i, 0] = value
            
            # print the resulting matrix





            
            #for i in range(rows):
            #    row_values = []
            #    for j in range(cols):
            #        # calculate the value for the (i,j) element
            #        value = (i+1)*(j+1)
                    # append the value to the current row
            #        row_values.append(value)
                # append the row to the matrix
            #    matrix_values.append(row_values)

                # convert the list of lists to a NumPy array
            #    matrix = np.array(matrix_values)
                    
                # print the resulting matrix
            #    print(matrix)

            
            
            # add new data to column 'A' using a for loop
            #for i in range(len(new_data)):
              #  df.loc[i, 'A'] = new_data[i]
                
        except KeyError:
            print("duration_in_traffic")
            break

#route = directions_result[0]['legs'][0]
#print("Route duration: {} minutes".format(route['duration']['text']))
#print("Route distance: {} miles".format(route['distance']['text']))
#print("Traffic: {}".format(route['duration_in_traffic']['text']))
matrix_values
df_final = pd.DataFrame(matrix_values)
df_final
