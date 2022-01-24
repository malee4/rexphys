# import packages
import numpy as np
import csv
import pandas as pd

# this assumes the central index is of distance greater than 3 from either end
# finds the normalized amplitude for the given set of data
def maximum(time, position, central_index, normal):
    x = time[central_index - 3: central_index + 4]
    y = position[central_index - 3: central_index + 4]
    values = np.polyfit(x, y, 2)
    a = values[0]
    b = values[1]
    c = values[2]
    
    central_x = (-1.0 * b) / (2.0 * a)
    central_y = (a * pow(central_x, 2) + b * central_x + c)
    return [central_x, central_y]


# finds the time near the extrema for the given set of data
def findExtrema(time, position, velocity, normal):
    extrema = {}
    current_sign = int(velocity[0] / abs(velocity[0]))
    index = 0
    
    
    
    for item in velocity:
        if int(item / abs(item)) == (-1 * current_sign):   
            # add it to the list of indices
            temp = maximum(time, position, index, normal) #temp[0] = time, temp[1] = amplitude
            extrema[temp[0] + normal / 100000000] = abs(temp[1]) #the addition of normal / 10000 is to prevent duplicate entries, change should be negligible
            # calculate the maximum
            current_sign = current_sign * -1
        index = index + 1
    return extrema

# data <- read in csv
path = open('C:\\Users\\melod\\2122\JTerm\\all_averages.csv')
cartData = pd.read_csv(path)
time = cartData['time']

position_15cm = cartData['15cm']
position_20cm = cartData['20cm']
position_25cm = cartData['25cm']
position_30cm = cartData['30cm']
position_35cm = cartData['35cm']

velocity_15cm = cartData['15cm_vel']
velocity_20cm = cartData['20cm_vel']
velocity_25cm = cartData['25cm_vel']
velocity_30cm = cartData['30cm_vel']
velocity_35cm = cartData['35cm_vel']

fifteen = findExtrema(time, position_15cm, velocity_15cm, 0.15)
twenty = findExtrema(time, position_20cm, velocity_20cm, 0.20)
twenty_five = findExtrema(time, position_25cm, velocity_25cm, 0.25)
thirty = findExtrema(time, position_30cm, velocity_30cm, 0.30)
thirty_five = findExtrema(time, position_35cm, velocity_35cm, 0.35)
    
write_path = open('C:\\Users\\melod\\2122\JTerm\\regular_found_extrema.csv', 'w')

writer = csv.writer(write_path)

#print(len(fifteen))
#print(len(twenty))
#print(len(twenty_five))
#print(len(thirty))
#print(len(thirty_five))

for item in fifteen:
    writer.writerow([item, fifteen[item], 15])
    
for item in twenty:
    writer.writerow([item, twenty[item], 20])
    
for item in twenty_five:
    writer.writerow([item, twenty_five[item], 25])
    
for item in thirty:
    writer.writerow([item, thirty[item], 30])

for item in thirty_five:
    writer.writerow([item, thirty_five[item], 35])
    
path.close()
write_path.close()
