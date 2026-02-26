import os
# 'bicycle' 'cars' 'Motorcycles' 'Bus' 'Trucks'
f = open("countv.txt", "r")
Lines = f.readlines()
count=0
myallowedveh = ['car', 'bike', 'bus', 'truck']
for line in Lines:
    count=count+1
    #print("Line{}: {}".format(count, line.strip()))
    words = line.split()
    for veh in myallowedveh:
        for j in range(1,int(words[myallowedveh.index('bus')+1])):
            print(veh)
#print('Number of words in text file :', len(words))
f.close()

