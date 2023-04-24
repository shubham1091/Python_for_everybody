
# 10.2 Write a program to read through the mbox-short.txt and figure out 
# the distribution by hour of the day for each of the messages. You can 
# pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out 
# the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "../Data/mbox-short.txt"
    
handle = open(name)

dc = dict()
for line in handle:
    if line.startswith("From: "):
        continue
    if line.startswith("From"):
        word = line.split()
        tm = word[5].split(":")
        hour = tm[0]
        dc[hour] = dc.get(hour,0) + 1

tp = sorted(dc.items())
for (k,v) in tp:
    print(k,v)