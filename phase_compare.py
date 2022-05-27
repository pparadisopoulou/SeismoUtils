import os
from sys import argv
from datetime import datetime
date_part =""
time_part =""
thessaloniki = []
with open(argv[2], "r") as f:
    for line in f.readlines():
        if ('    Date                   ' in line):
            date_part = line[27:].replace('\n','')
           # print(date_part)
        if '    Time                   ' in line:
            time_part = line[27:37].replace('\n','')
            #print (time_part)
        if date_part !="" and time_part !="":
            thessaloniki.append (datetime.strptime("{0} {1}".format(date_part,time_part),"%Y-%m-%d %H:%M:%S.%f"))
       
print (len(thessaloniki))
with open(argv[1], "r") as f:
    lines = f.read()
    data = lines.split('\n\nSTOP\n\n')
    data = list(filter(None,data))
    for item in data[1:]:
        temp = item.splitlines()[5]
        temp = list(filter(None , temp.split(' ')))
        event_ath = (datetime.strptime("{0} {1}".format(temp[0],temp[1]),"%Y/%m/%d %H:%M:%S.%f"))
        
        for thess in thessaloniki:
            diff = thess - event_ath
            if (abs(diff.total_seconds()) < 1):
                print("FOUND")
                break