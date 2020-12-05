"""
@author: Tehreem Tungekar
This program analyzes and visualizes data obtained from Fitbit
To run this program, go to your terminal window and type 'pip install matplotlib'
Then type python3 analyze.py to run this program
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from datetime import datetime 

df= pd.DataFrame()
# Read data from csv file three_month_data_fitbit.csv
df = pd.read_csv('three_month_data_fitbit.csv')

#=========PART1: Pie chart comparison for activity========
#Sedentary minutes is the time user was sitting/not involved in any physical activity
#Very Active minutes are the ones where the user was very actively doing some physical activity
#Lightly Active minutes denote the time when the user was doing very light physical work
#Fairly Active minutes also denote very little physical activity

#List to store labels
Minute_Names=['Very Active', 'Lightly Active', 'Fairly Active']

#Calculate sum of all activities
very_act_sum=df['Very Active Minutes'].sum()
light_act_sum= df['Lightly Active Minutes'].sum()
fair_act_sum= df['Fairly Active Minutes'].sum()

#Storing activities' sum in a list
Minute_Data=[very_act_sum, light_act_sum, fair_act_sum]
explode = (0.1, 0, 0)

plt.pie(Minute_Data,labels=Minute_Names, autopct='%1.1f%%', shadow=True, explode=explode)
plt.title("Tehreem's Activity Distribution for June, July & August 2020")
plt.legend(loc='best')
plt.show()

#========PART2: Daily Average Distance Distribution=======

#Getting distance and grouping it by month
dist=df['Distance(miles)']

dist_june=dist.iloc[0:30]
dist_july=dist.iloc[30:61]
dist_aug=dist.iloc[61:92]

#Getting days of the three months
df['Day']=[d.split('-')[2] for d in df['Date']]
dates=df['Day']

days_june= dates.iloc[0:30]
days_july= dates.iloc[30:61]
days_aug= dates.iloc[61:92]

plt.bar(days_june, dist_june, color='#ADD8E6')
plt.xlabel('Days in June')
plt.ylabel('Distance (in miles)')

blue_patch = mpatches.Patch(color='#ADD8E6', label='Distance covered(in miles)')
green_line = mlines.Line2D([], [], color='green', linestyle='dashed', markersize=15, label='Daily goal: 5 miles')
plt.legend(handles=[blue_patch, green_line])
plt.axhline(y=5, color='green', linestyle='--')
plt.title('Distance Distribution for all days in June')
plt.show()

plt.bar(days_july, dist_july, color='#ADD8E6')
plt.legend(handles=[blue_patch, green_line])
plt.axhline(y=5, color='green', linestyle='--')
plt.xlabel('Days in July')
plt.ylabel('Distance (in miles)')
plt.title('Distance Distribution for all days in July')
plt.show()

plt.bar(days_aug, dist_aug, color='#ADD8E6')
plt.legend(handles=[blue_patch, green_line])
plt.axhline(y=5, color='green', linestyle='--')
plt.xlabel('Days in August')
plt.ylabel('Distance (in miles)')
plt.title('Distance Distribution for all days in August')
plt.show()

#=======PART3: Comparison of Sedentary Minutes with Active Minutes=====
sed_min=df['Sedentary Minutes']

sed_june= sed_min.iloc[0:30]
sed_july= sed_min.iloc[30:61]
sed_aug= sed_min.iloc[61:92]

very_act=df['Very Active Minutes']

very_act_june= very_act.iloc[0:30]
very_act_july= very_act.iloc[30:61]
very_act_aug= very_act.iloc[61:92]

light_act=df['Lightly Active Minutes']

light_act_june= light_act.iloc[0:30]
light_act_july= light_act.iloc[30:61]
light_act_aug= light_act.iloc[61:92]

fair_act=df['Fairly Active Minutes']

fair_act_june= fair_act.iloc[0:30]
fair_act_july= fair_act.iloc[30:61]
fair_act_aug= fair_act.iloc[61:92]

fig1 = plt.figure()
ax = fig1.add_subplot(1,1,1)


#Comparison for June
ax.scatter(days_june, sed_june, color='red', label='Sedentary Minutes')
ax.scatter(days_june,very_act_june, color='green', label='Very Active Minutes')
ax.scatter(days_june,light_act_june, color='blue', label='Lightly Active Minutes')
ax.scatter(days_june, fair_act_june, color='gray', label='Fairly Active Minutes')
plt.xlabel('Days in June')
plt.ylabel('Minutes')
plt.title('Comparison of Sedentary Minutes with Active Minutes for June')
plt.legend(loc='best', fontsize='7')
plt.show()

#Comparison for July
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)

ax2.scatter(days_july, sed_july, color='red', label='Sedentary Minutes')
ax2.scatter(days_july,very_act_july, color='green', label='Very Active Minutes')
ax2.scatter(days_july,light_act_july, color='blue', label='Lightly Active Minutes')
ax2.scatter(days_july, fair_act_july, color='gray', label='Fairly Active Minutes')
plt.xlabel('Days in July')
plt.ylabel('Minutes')
plt.title('Comparison of Sedentary Minutes with Active Minutes for July')
plt.legend(loc='best', fontsize='7')
plt.show()

#Comparison for August
fig3 = plt.figure()
ax3 = fig3.add_subplot(1,1,1)

ax3.scatter(days_aug, sed_aug, color='red', label='Sedentary Minutes')
ax3.scatter(days_aug,very_act_aug, color='green', label='Very Active Minutes')
ax3.scatter(days_aug,light_act_aug, color='blue', label='Lightly Active Minutes')
ax3.scatter(days_aug, fair_act_aug, color='gray', label='Fairly Active Minutes')
plt.xlabel('Days in August')
plt.ylabel('Minutes')
plt.title('Comparison of Sedentary Minutes with Active Minutes for August')
plt.legend(loc='best', fontsize='7')
plt.show()

#========PART4: Sleep time analysis========
sleep_start=df['Sleep Start(Time)']

sleep_start_june= sleep_start.iloc[0:30]
sleep_start_july= sleep_start.iloc[30:61]
sleep_start_aug= sleep_start.iloc[61:92]

#For June:
plt.barh(days_june,sleep_start_june, color='lavender')
for index, value in enumerate(sleep_start_june):
    plt.text(value, index-0.25, str(value), fontsize='7')

lavender_patch = mpatches.Patch(color='lavender', label='Sleep start time in 24-hr format')
plt.legend(loc='lower right',handles=[lavender_patch])
plt.xlabel('Sleep Start Time in HH:MM')
plt.ylabel('Days in June')
plt.title('Sleep Start Time Analysis for June')
plt.show()

#For July:
plt.barh(days_july,sleep_start_july, color='lavender')
for index, value in enumerate(sleep_start_july):
    plt.text(value, index-0.25, str(value), fontsize='7')
plt.legend(loc='lower right',handles=[lavender_patch])
plt.xlabel('Sleep Start Time in HH:MM')
plt.ylabel('Days in July')
plt.title('Sleep Start Time Analysis for July')
plt.show()

#For August:
plt.barh(days_aug,sleep_start_aug, color='lavender')
for index, value in enumerate(sleep_start_aug):
    plt.text(value, index-0.25, str(value), fontsize='7')
plt.legend(loc='lower right',handles=[lavender_patch])
plt.xlabel('Sleep Start Time in HH:MM')
plt.ylabel('Days in August')
plt.title('Sleep Start Time Analysis for August')
plt.show()

#==========PART5: Correlation between Distance and Calories Burnt

calorie=df['Calorie Count(cals)']

cal_june= calorie.iloc[0:30]
cal_july= calorie.iloc[30:61]
cal_aug= calorie.iloc[61:92]


fig4 = plt.figure()
ax4 = fig4.add_subplot(1,1,1)
ax4.scatter(dist_june, cal_june, color='maroon', label='Days in June')
ax4.scatter(dist_july,cal_july, color='purple', label='Days in July')
ax4.scatter(dist_aug,cal_aug, color='green', label='Days in Aug')
plt.xlabel('Distance (in miles)')
plt.ylabel('Calories Burnt (in cals)')
plt.title('Correlation of Distance with Calories burnt per day for June, July & August')
plt.legend(loc='best', fontsize='7')
plt.show()

#=======PART6: Plotting variations based on various days of the week
#Calculating weekday:
df['Weekday'] = df['Date'].map(lambda x: (datetime.strptime(str(x),"%Y-%m-%d")).weekday())
weekday_steps = df['Steps(Count)'].groupby(df['Weekday']).mean()

fig5,axes = plt.subplots(figsize=(12, 4), nrows=1, ncols=3)

plt.sca(axes[0])
weekday_steps.plot(kind = 'bar',color = '#136207', alpha = 0.5)
plt.ylabel('Average number of steps')
plt.title('Daily average number of steps walked')
plt.axhline(y=6000, color='pink', linestyle='--')
plt.xticks(list(range(7)),['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
plt.legend()

sleep_minutes_mean = df['Minutes Asleep'].groupby(df['Weekday']).mean()/60

plt.sca(axes[1])
sleep_minutes_mean.plot(kind = 'bar',color = 'brown', alpha = 0.5, label='Hours Asleep')
plt.ylabel('Average number of hours slept')
plt.title('Daily average number of hours slept')
plt.axhline(y=7, color='green', linestyle='--')
plt.xticks(list(range(7)),['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
plt.legend()

water_med = df['Water Intake(oz)'].groupby(df['Weekday']).mean()

plt.sca(axes[2])
water_med.plot(kind = 'bar',color = '#0f52ba', alpha = 0.5)
plt.ylabel('Average ounces of water intake')
plt.title('Daily average ounces of water intake')
plt.axhline(y=74, color='purple', linestyle='--')
plt.xticks(list(range(7)),['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
plt.legend()
plt.show()


