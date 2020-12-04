"""
This program is used to collect data from Fitbit using Fitbit API.
It collects date, steps, distance, calorie count, sedentary minutes, very active minutes,
lightly active minutes, fairly active minutes, minutes asleep, sleep start time and daily water intake
and stores it in a csv file named 'three_month_data_fitbit.csv'.
It also collects a day's data like the step count, calorie count and distance measured every 15 mins
and stores it in a csv file named 'single_day_data_fitbit.csv'
To run this program, first create a Fitbit account and get your CLIENT_ID and CLIENT_SECRET,
then run gather_keys_oauth2.py(developed by Python API developers) program to get your access token
and refresh token. 
After getting the tokens, in your terminal window, type command 'pip install' to install the following
libraries: fitbit, datetime, pandas and csv.
Collects data for the months- June, July & August 2020
@author: Tehreem Tungekar
"""
#Importing libraries
import fitbit
import datetime
import csv
import pandas as pd

#Declaring tokens
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOU_CLIENT_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
REFRESH_TOKEN = 'YOUR_REFRESH_TOKEN'

#Connecting with Fitbit's API
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

#Collecting data for the past 100 days, so initializing dates
hundred = str((datetime.datetime.now() - datetime.timedelta(days=186)).strftime("%Y-%m-%d"))    #should be in yy-mm-dd format
today = str((datetime.datetime.now() - datetime.timedelta(days=95)).strftime("%Y-%m-%d"))

#Creating dataframe in pandas to eliminate for loops
df = pd.DataFrame()

#=======PART1: Collecting Distance data==========
distance = auth2_client.time_series('activities/distance', base_date=hundred, end_date=today)

#date_list will store all the dates
date_list = []    

for d in distance['activities-distance']:
    date_list.append(d['dateTime'])
      
df = pd.DataFrame (date_list,columns=['Date'])

#Storing Distance in miles using dataframe
df['Distance(miles)'] = pd.DataFrame(distance['activities-distance'])['value'].astype(float)

#========PART2: Collecting Calorie in cals unit=========
calories = auth2_client.time_series('activities/calories', base_date=hundred, end_date=today)

df['Calorie Count(cals)'] = pd.DataFrame(calories['activities-calories'])['value'].astype(int)

#========PART3: Collecting Step data=========
steps= auth2_client.time_series('activities/steps', base_date=hundred, end_date=today)

df['Steps(Count)'] = pd.DataFrame(steps['activities-steps'])['value'].astype(int)

#========PART4: Collecting Sedentary Minutes data=========
min_sed= auth2_client.time_series('activities/minutesSedentary', base_date=hundred, end_date=today)

df['Sedentary Minutes'] = pd.DataFrame(min_sed['activities-minutesSedentary'])['value'].astype(int)

#========PART5: Collecting Very Active Minutes data=========
min_active= auth2_client.time_series('activities/minutesVeryActive', base_date=hundred, end_date=today)

df['Very Active Minutes'] = pd.DataFrame(min_active['activities-minutesVeryActive'])['value'].astype(int)

#=======PART6: Collecting Lightly Active Minutes data======
min_light= auth2_client.time_series('activities/minutesLightlyActive', base_date=hundred, end_date=today)

df['Lightly Active Minutes'] = pd.DataFrame(min_light['activities-minutesLightlyActive'])['value'].astype(int)

#=======PART7: Collecting Fairly Active Minutes data======
min_fair= auth2_client.time_series('activities/minutesFairlyActive', base_date=hundred, end_date=today)

df['Fairly Active Minutes'] = pd.DataFrame(min_fair['activities-minutesFairlyActive'])['value'].astype(int)

#=======PART8: Collecting Sleep data========
asleep = auth2_client.time_series('sleep/minutesAsleep', base_date= hundred ,end_date=today)
df['Minutes Asleep'] = pd.DataFrame(asleep['sleep-minutesAsleep'])['value']

sleep_start = auth2_client.time_series('sleep/startTime', base_date= hundred ,end_date=today)
df['Sleep Start(Time)'] = pd.DataFrame(sleep_start['sleep-startTime'])['value']

#========PART09: Collecting Water Intake
water = auth2_client.time_series('foods/log/water',base_date=hundred, end_date=today)
df['Water Intake(oz)'] = pd.DataFrame(water['foods-log-water'])['value'].astype(float)
#print(water)

#Creating and opening a new csv file to write data for 100 days
with open('three_month_data_fitbit.csv', "w") as f:
    df.to_csv(f, header=True,index = False,  line_terminator='\n')
    

#==========Collecting a day's data for further analysis========
df_day = pd.DataFrame() #New dataframe to store a day's data

t=str((datetime.datetime.now()).strftime("%Y-%m-%d")) 

#========PART1: Collecting step count for every 15 min during a day
steps_day = auth2_client.intraday_time_series('activities/steps',base_date=t, detail_level='15min')

df_day['Time'] = pd.DataFrame(steps_day['activities-steps-intraday']['dataset'])['time']
df_day['Step Count']=pd.DataFrame(steps_day['activities-steps-intraday']['dataset'])['value']

#=======PART2: Collecting calorie information
cal_day = auth2_client.intraday_time_series('activities/calories',base_date=t, detail_level='15min')
df_day['Calorie Count'] = pd.DataFrame(cal_day['activities-calories-intraday']['dataset'])['value'].astype(int)

#=======PART3: Collecting Distance information   
distance_day = auth2_client.intraday_time_series('activities/distance',base_date=t, detail_level='15min')
df_day['Distance(miles)'] = pd.DataFrame(distance_day['activities-distance-intraday']['dataset'])['value'].astype(float)

#-----------Elevation and floor information is only available for Fitbit compatible device owners
# Fitbit is not compatible with my Samsung phone sensors  
#=======PART4: Collecting Elevation info
#elevation_day = auth2_client.intraday_time_series('activities/',base_date=t, detail_level='15min')        
#print(elevation_day)      
#df_day['Elevation'] = pd.DataFrame(elevation_day['activities-elevation-intraday']['dataset'])['value'].astype(float)

#=======PART5: Collecting Floor count
#floor_day = auth2_client.intraday_time_series('activities/floors',base_date=t, detail_level='15min')
#df_day['Floors Count'] = pd.DataFrame(floors_day['activities-floors-intraday']['dataset'])['value'].astype(int)

#


with open('single_day_data_fitbit.csv', "w") as f:
    df_day.to_csv(f, header=True,index = False,  line_terminator='\n')
