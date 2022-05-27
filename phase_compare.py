import os
from sys import argv
from datetime import datetime
date_part =""
time_part =""
thessaloniki = []
with open(argv[2], "r") as f:
    counter =0
    for line in f.readlines():
        if ('    Date                   ' in line):
            date_part = line[27:].replace('\n','')
            counter +=1
           # print(date_part)
        if '    Time                   ' in line:
            time_part = line[27:37].replace('\n','')
            #print (time_part)
            thessaloniki.append (datetime.strptime("{0} {1}".format(date_part,time_part),"%Y-%m-%d %H:%M:%S.%f"))
       
print (counter)
print (len(thessaloniki))
with open(argv[1], "r") as f:
    lines = f.read()
    data = lines.split('\n\nSTOP\n\n')
    data = list(filter(None,data))
    print (len(data))
    for item in data[1:1203]:
        temp = item.splitlines()[5]
        temp = list(filter(None , temp.split(' ')))
        event_ath = (datetime.strptime("{0} {1}".format(temp[0],temp[1]),"%Y/%m/%d %H:%M:%S.%f"))
        
        for event_thess in thessaloniki:
            diff = event_thess - event_ath
            if (abs(diff.total_seconds()) < 2):
               # print("FOUND")
                data.remove(item)
                break
print(len(data))
with open('results.txt', 'w') as f:
    for item in data:
        f.write("%s" % item)