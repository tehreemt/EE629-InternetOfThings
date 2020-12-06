
Project Title: **"Using Fitbit's API to Acquire, Visualize, and Analyze Data in Python"**

Status: **Completed**

Fitbit provides a Web API to access data from Fitbit activity trackers, Aria & Aria 2 scales, or manually entered logs.
Fitbit API (https://dev.fitbit.com/build/reference/web-api/basics/) can be used to get your own data.

I have a **Samsung Galaxy smartwatch** which has Step Tracker sensor. I also use my **Samsung Galaxy S8+ phone**, which is capable of tracking a my steps through the S Health app.

Step 1: Create your [Fitbit account](https://accounts.fitbit.com/signup?targetUrl=https%3A%2F%2Fwww.fitbit.com%2Flogin%2Ftransferpage%3Fredirect%3Dhttps%253A%252F%252Fwww.fitbit.com&lcl=en_US):

![](createFitbitAccount.PNG)

Enter all your information like Name, Date of birth, height, weight and click on "Join Fitbit".

Step 2: Set up your account by verifying your email. Go to your Dashboard:

![](fitbitDashboard.PNG)

Go to https://dev.fitbit.com/
Go to “Manage” and click on “Register An App":

![](registerApp.PNG)

Fill in all the details on the Registration page:

![](registrationInfo.PNG)

The next page will have all your details like OAuth Client ID and Client Secret.
I have hidden those details for security reasons.

![](authDetails.PNG)

Step 3: Install the Fitbit API Python Library:

Navigate to https://github.com/orcasgit/python-fitbit and install fitbit python library by downloading the zip file and running the following command on your terminal.
cd to your path which contains the downloaded zip file and type:

~sudo pip install -r requirements/base.txt

![](installLibrary.PNG)

Once this step is done, you can start writing your code using fitbit api library.

Step 4: Role of OAuth in Authorization:
Once fitbit API library is installed from the previous step, now the only thing thats remaining is getting access token and refresh token to keep on refreshing that access token. 
Access tokens are like temporary keys which are asigned so that you can access a specific set of resources for a specific period of time. You can only get these tokens when you have convinced the Fitbit server that you are who you say you are! i.e. authenticated yourself successfully. 
So, to get these access tokens, navigate to file named gather_keys_oauth2.py which can be found in the python folder that we downloaded in the previous step. Go to cmd and type ther following command (Remember to put your own Client Id and Client secret which you obtained in step 1):

~python gather_keys_oauth2.py <"CLIENT ID"> <"CLIENT SECRET"> 

You would be automatically redirected to the fitbit Authentication page where it would ask you to authenticate yourself(by providing your username & password). Then, you will be asked to select the resources you want the program to access. I have selected all resources as can be seen below:

![](oauth.PNG)

Once successfully authenticated (ONLY after successful authentication), you will see the tokens in your terminal(Hidden for security). 
'expires_in' denotes when the token is set to expire;
'refresh_token' is the token which would be used to refresh our access token (when it expires);
'scope' denotes all the fields it would have access to. Notice that this is the same as I selected in the previous step.

![](oAuthTokens.PNG)




Step 5: Run collect_data.py program in your terminal window by typing python3 collect_data.py:
The .csv files would be generated.

Step 6: Run analyze.py in your terminal window by typing python3 analyze.py:

i. The first pie chart with Activity Distribution will be generated:

![](1.Activity_Distribution.PNG)

ii. The following graphs show distance distribution for three months, namely, June, July and August 2020:

  a. Distance distribution for the month of June:
  
  ![](2a.Distance_June_All_Days.PNG)
  
  b. Distance distribution for the month of July:
  
  ![](2b.Distance_July_All_Days.PNG)
  
  c. Distance distribution for the month of August:
  
  ![](2c.Distance_Aug_All_Days.PNG)

iii. Next, I compared my sedentary minutes with active ones. Fitbit categorizes Active minutes as Very Active, Lightly Active and Fairly Active. Fitbit categorizes time as 'Sedentary minutes' when the user is sitting.
The following graphs show comparison between active minutes and sedentary minutes for June, July and August.

  a. Comparison scatter plot for Sedentary Minutes and Active Minutes for the month of June:
  
  ![](3a.SedvsAct_June.PNG)
  
  b. Comparison scatter plot for Sedentary Minutes and Active Minutes for the month of July:
  
  ![](3b.SedvsAct_July.PNG)
  
  c. Comparison scatter plot for Sedentary Minutes and Active Minutes for the month of August:
  
  ![](3c.SedvsAct_Aug.PNG)
  
  The scatter plot shows I have been less active for all the three months; being most sedentary in the month of August.
  
iv. A Harvard study conducted on 61 undergraduate student concluded that students with irregular patterns of sleep and wakefulness had a lower grade point average than the rest. So, its a very essential metric to take into account.
 I compared my sleep start times for all the three months and it is evident that my sleeping pattern can be improved.
 
  Sleep Start Time Analysis for June, July & August 2020:
  
  ![](4.Sleep_StartTime_Frequency.PNG)
  
 v. Whether you work out in a gym or you run in a park, the more you workout, the more calories are burnt. Let us see the correlation of distance and calorie burnt by analyzing data for all three months. 
 
  Correlation of Distance with Calories burnt per day:
  
  ![](5.Correlation_Cal_Dist.PNG)
  
  It is important to find correlation between calories burnt per day vs workout. It can be seen that the more I worked out, the more calories I burnt.
  
 vi. Analysis based on weekdays for all the three months:
 
  ![](6.Average_Step_Sleep_Water.PNG)
  
  a. My goal is to walk atleast 6000 steps daily. 10,000 is the recommended number, but since I have been busy lately, my daily step target is 6000. The first bar chart shows average number of daily steps based on weekdays. Mondays, Sundays and Saturdays are the three days where my average steps are above my goal of 6000 steps. Thursday has the least number of average steps as I have my office hours on Thursdays so I usually am indoors.
  
  b. Next, I analyzed my sleep hours based on weekdays. 7-9 hrs of sleep is recommended for a healthy body and healthy mind. On an average, Tuesdays, Thursdays and Saturdays are the days I get enough sleep. It can be seen from the second chart that I get less sleep usually on Thursdays, since Thursday is my busiest day.
  
  c. Moving on to water intake analysis, which I think is often not taken into consideration, but is the most important element to stay healthy. For women, 74oz of water intake is recommended to stay healthy. Definitely, I'll have to drink more water as my average water intake seems to be low on all days except Fridays.
 
