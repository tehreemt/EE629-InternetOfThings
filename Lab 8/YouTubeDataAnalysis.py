#@authortehreemtungekar
""" This program is a python script to take input from user as a search term and maximum number
    of records to be displayed. Once the user enters this information,
    it searches using YouTube API and stores the results in a .csv file.
    Once the results are stored successfully, analysis is performed on them. 
    Firstly, all the videos are displayed in the terminal sorted by newest videos first. 
    Next, top 5 highest videos are printed, followed by top 5 ones with highest percentage of views.
    First of all please run pip install csv, pip install csv and pip install pandas to install the libraries necessary
    to run this program.
    To run this program from the terminal, type python youtube_searchfinal.py and hit enter. You will be
    prompted for a search term and a maximum number of records you want to retrieve.
    """

from googleapiclient.discovery import build
import csv
import unidecode                        #reference: StackOverflow
import sys,csv,operator
import pandas as pd                     #This library makes it easy to manipulate .csv data

API_KEY = "YOUR API KEY HERE"     #My developer account API KEY

API_NAME = "youtube"
API_VERSION = "v3" 

def youtube_search(num,i):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(q=i, part="id,snippet", maxResults=num).execute()
    videos = []  
    # create a CSV output for output with list of videos   
    csvFile = open('tungekar_hw3.csv','w')
    csvWriter = csv.writer(csvFile)         
    csvWriter.writerow(["id","publishedAt","title","duration","viewCount","likeCount"])    
    # Add each result to the appropriate list, and then display the lists of matching videos
    for search_instance in search_response.get("items", []):
        if search_instance["id"]["kind"] == "youtube#video":
            title = search_instance["snippet"]["title"]
            title = unidecode.unidecode(title) 
            
            videoId = search_instance["id"]["videoId"]
            publishedAt = search_instance["snippet"]["publishedAt"]
            video_response = youtube.videos().list(id=videoId,part="statistics").execute()
           
            duration_response = youtube.videos().list(id=videoId,part="contentDetails").execute()
            
            for duration_result in duration_response.get("items",[]):   #get duration of all returned videos
                duration = duration_result["contentDetails"]["duration"]
             
            for video_result in video_response.get("items",[]):
                
                viewCount = video_result["statistics"]["viewCount"]
                if 'likeCount' not in video_result["statistics"]:       #if there are no likes, it is 0
                    likeCount = 0
                else:
                    likeCount = video_result["statistics"]["likeCount"]
                
            csvWriter.writerow([videoId,publishedAt,title,duration,viewCount,likeCount])
           
    csvFile.close()

##The above function retrieved the list of videos and wrote them in the csv file

#This function is used to print the results from csv file sorted by newest videos first
#I tried using sortedlist/sorted functions, but got some errors and the result was not pretty.
#Using pandas, the result looks much pretty and readable
def printNewSort():
    fi= open('tungekar_hw3.csv')       
    di = pd.read_csv (fi)       #creating dataframe object
    di = di.dropna()            #deleting all empty rows in dataframe as they interfere with sorting
    di.to_csv(index=False)      #By default, pandas dataframe has index, we dont want to display that in our result so remove it
    di = di.dropna()            #deleting cells again after removing index
    pd.set_option("display.max_rows", None, "display.max_columns", None)   #If this step is missed, dataframe is displayed in bits and pieces
    sorted_di = di.sort_values(by=['publishedAt'], ascending=False)     #sorting dataframe by date published at, ascending is newest first
    print((sorted_di[[ 'id','publishedAt','title','duration','viewCount','likeCount']]).to_string(index=False)) #printing result,without index
    
#The following function is used to print first five highest viewed videos 
#It sorts based on colum viewCount
def printHighFive():
    fi= open('tungekar_hw3.csv')       
    di = pd.read_csv (fi)
    di = di.dropna()
    di.to_csv(index=False)
    di = di.dropna()
    #Since rank from 1 to 5 is to be printed, declare it and initialize it to dataframe 
    di['Rank']= di['viewCount'].rank(ascending=False)   
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    sorted_di = di.sort_values(by=['viewCount'], ascending=False)   #Sorting by viewCount column, similar to previous function
    #While displaying the dataframe, use head(5) because we just want to display first 5 video records
    print((sorted_di[['Rank','title', 'id','publishedAt','title','duration','viewCount']].head(5)).to_string(index=False))

#Function printHighPercentageFive prints the first five videos with highest percentage of views
#Percentage is calculated by likeCount/viewCount
#It prints the results sorted by highest percentage 
def printHighPercentageFive(): 
    f = open('tungekar_hw3.csv')
    df = pd.read_csv (f)
    highPer =  df["likeCount"]/df["viewCount"]  #Calculating highest percentage using two columns of dataframe
    df["highestPercentage"] = highPer           #Assigning the previously calculated percentage to one new column in dataframe
    df.to_csv(index=False)
    df = df.dropna()
    df['Rank']= df['highestPercentage'].rank(ascending=False)       #Making a new column for Rank in the dataframe
    df.astype({'Rank': 'int'})                  #This did not work, but I still added it for my reference. It was supposed to display rank as integer
    df.to_csv(index=False)
    df = df.reset_index(drop=True)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    sorted_df = df.sort_values(by=['highestPercentage'], ascending=False)  #Sorting the dataframe by highestPercentage column
    print("Sorted by Highest Percentage: Calculated by computing Highest Percentage= likeCount/viewCount.")
    print("The top 5 results are:\n")
    print((sorted_df[['Rank','title', 'id','highestPercentage','viewCount','likeCount','publishedAt','duration']].head(5)).to_string(index=False))


 

if __name__ == "__main__":
    str_term = str(input("Please enter a search term: "))
    search_Num=int(input("Please enter the maximum number of results to display: "))
    print("Searching for: ",str_term,"Maximum records to be searched: ",search_Num)
    youtube_search(search_Num,str_term)
    print("\n This is the result for all videos retrieved, sorted by newest first:\n")
    printNewSort()  
    print("\n This is the result for top 5 videos retrieved, sorted by highest viewed videos first:\n")
    printHighFive()
    print("\n This is the result for top 5 videos retrieved, sorted by highest viewed percentage videos first:\n")
    printHighPercentageFive()