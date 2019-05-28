import urllib.request
import json
import time
import os


name1="pewdiepie"
name2="tseries"
timee = int(input("Enter the show time in mins: "))
key = "PUT YOUR GOOGLE API KEY HERE"
timee = timee*60
i = 0
while i <= timee:

    data1 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+"pewdiepie"+"&key="+key).read()
    data2 =  urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+"TSeries"+"&key="+key).read()


    subs1 = json.loads(data1)["items"][0]["statistics"]["subscriberCount"]
    subs2 = json.loads(data2)["items"][0]["statistics"]["subscriberCount"]

    print("\r pewdiepie has got "+subs1+" right now! ", end='')
    print("\r Tseries has got " + subs2 + "right now!",end='')

    int_subs1= int(subs1)
    int_subs2 = int(subs2)

    diff = int_subs2-int_subs1
    
    str_diff = str(diff)

    print("\r pewdiepie lags by " + str_diff + " subscribers",end='')
    
    time.sleep(1)
    i = i+1
