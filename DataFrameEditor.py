import numpy as np
import pandas as pd



#TO DO
#Date DONE
#time from 9 pm DONE
#Sleep Score DONE
#weekdays DONE

# returns minutes after 9 p.m. I fell asleep 
def diffInMin(time): 
    hour = int(time[-5:-3]) #hour fell asleep
    minute = int(time[-2:]) #minutes in time stamp
    if hour >= 9:
        minutesOfHour = 60* (hour - 9)
    else:
        minutesOfHour = 60* (hour + 3)
    return(minutesOfHour + minute)

def weekDay(date):
    d = pd.Timestamp(date)
    return(d.dayofweek)


#modifies topics 
df = pd.read_csv("FitBitSleepCsv/fitbit_export_20230126-5.csv")
df['Date'] = df['Unnamed: 0'].str[:10] #seperates by data
df['Sleep Time'] = df['Unnamed: 0'].str[10:-2] #seperates by time asleep
df['Minutes after 9 pm'] = df['Sleep Time'].apply(diffInMin) #finds minutes after 9PM
df['Weekday'] = df['Date'].apply(weekDay)#fins week day(Monday = 0, tues = 1 ...)
df.set_index('Date', inplace = True)#makes date the index of the df
df = df.drop('Unnamed: 0', axis = 1)#removes sleep time
df['Awake Time'] = df['End Time'].str[10:-2] #creates awake time
df = df.drop('End Time', axis =1) #removes end time
df['Sleep Score'] = [72,88,80,79,81,84] #,anually add sleepscore 
print(df)
df.to_csv('EditedCSVfiles/EarlyDECsleep.csv')#exports to csv


