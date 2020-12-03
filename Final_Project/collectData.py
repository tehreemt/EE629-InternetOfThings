"""
This program is used to collect data from Fitbit using Fitbit API.
It collects date, steps, distance, and calories and stores it in a csv file.
To run this program, first create a Fitbit account and get your CLIENT_ID and CLIENT_SECRET,
then run gather_keys_oauth2.py(developed by Python API developers) program to get your access token
and refresh token. 
After getting the tokens, in your terminal window, type command 'pip install' to install the following
libraries: fitbit, datetime and csv.
@author: Tehreem Tungekar
"""
#Importing libraries
import fitbit
import datetime
import csv

#Declaring tokens
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOU_CLIENT_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
REFRESH_TOKEN = 'YOUR_REFRESH_TOKEN'

#Using tokens to get data
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

#Collecting data for the past 100 days, so initializing dates
hundred = str((datetime.datetime.now() - datetime.timedelta(days=99)).strftime("%Y-%m-%d"))    #should be in yy-mm-dd format
today = str((datetime.datetime.now() - datetime.timedelta(days=0)).strftime("%Y-%m-%d"))

#=======PART1: Collecting Distance data==========
distance = auth2_client.time_series('activities/distance', base_date=fifty, end_date=today)

#date_list will store all the dates
date_list = ["Date"]    
#distance_list will store the total distance data
distance_list = ["Distance"]

for d in distance['activities-distance']:
    time_list.append(d['dateTime'])
    distance_list.append(d['value'])
    
#========PART2: Collecting Calorie data=========
calories = auth2_client.time_series('activities/calories', base_date=fifty, end_date=today)

#cal_list stores the calorie count
cal_list=["Calorie Count"]

for x in fit_statsCal['activities-calories']:
    cal_list.append(d['value'])

#Getting all the lists together to zip them
rows = zip(date_list,distance_list,cal_list)

#Creating and opening a new csv file to write data
with open('data_fitbit.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
   
   
    

