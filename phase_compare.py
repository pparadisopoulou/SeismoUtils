import os
import sys
from sys import argv
from datetime import datetime
date_part =""
time_part =""
thessaloniki = []

#added some comments
athens_file = input("Enter the filename for the Athens input file (Default value : IMS.txt)\n") or "IMS.TXT"
print(athens_file)
thessaloniki_file = input("Enter the filename for the Thessaloniki input file (Default value : bulletin_ALL.txt)\n") or "bulletin_ALL.txt"
print(thessaloniki_file)
output_file = input("Enter the filename for the output file (Default value : results.txt)\n") or "results.txt"
print(output_file)
diff_seconds = int(input("Enter the maximum difference in seconds between events timestamp (Default value : 2 seconds)\n") or "2")
print(diff_seconds)
with open(thessaloniki_file, "r") as f:
    counter =0
    for line in f.readlines():
        if ('    Date                   ' in line):
            date_part = line[27:].replace('\n','')
            counter +=1
    
        if '    Time                   ' in line:
            time_part = line[27:37].replace('\n','')
    
            thessaloniki.append (datetime.strptime("{0} {1}".format(date_part,time_part),"%Y-%m-%d %H:%M:%S.%f"))
       
print (counter)
print (len(thessaloniki))
with open(athens_file, "r") as f:
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
            if (abs(diff.total_seconds()) < diff_seconds):
               # print("FOUND")
                data.remove(item)
                break
print(len(data))
with open(output_file, 'w') as f:
    for item in data:
        f.write("%s" % item)