import csv
from sys import argv
if len(argv) <2 :
    print ("Usage : python split_map.py <step> <input_filename>")
    
with open(argv[2], "r") as f:
    reader = csv.DictReader(f)
    a = list(reader)

    maxlat = (float)(max(a, key=lambda x:x['lat'])["lat"])
    minlat = (float)(min(a, key=lambda x:x['lat'])["lat"])

    maxlon = (float)(max(a, key=lambda x:x['lon'])["lon"])
    minlon = (float)(min(a, key=lambda x:x['lon'])["lon"])
   # print (maxlat)
   # print (minlat)

    latstep = ((float)(maxlat) - (float)(minlat))/(int)(argv[1])
    #print (latstep)

    #print (maxlon)
    #print (minlon)

    lonstep = ((float)(maxlon) - (float)(minlon))/(int)(argv[1])
    #print (lonstep)

    
    for i in range((int)(argv[1])):
        for j in range((int)(argv[1])):
            #print ("{0} ---- {1}".format(i,j))
            for item in a:
                lat = (float)(item["lat"])
                lon = (float)(item["lon"])
                if lat>(minlat + i*latstep) and lat<= (minlat+(i+1)*latstep) and lon>(minlon +j*lonstep) and lon<=(minlon +(j+1)*lonstep):
                    print ("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(i,j,item["DAz"], item["dip"], item["rake"],item["No"]))

        



