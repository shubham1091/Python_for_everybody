
# 9.4 Write a program to read through the mbox-short.txt and figure out who 
# has sent the greatest number of mail messages. The program looks for 'From ' 
# lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. After the dictionary 
# is produced, the program reads through the dictionary using a maximum loop to 
# find the most prolific committer.


name = input("Enter file:")
if len(name) < 1:
    name = "../Data/mbox-short.txt"
handle = open(name)

dc = dict()
for line in handle:
    if line.startswith("From:"):
        sender = line.split()[1]
        dc[sender]=dc.get(sender,0)+1

add = ""
count = 0
for k,v in dc.items():
    if v>count:
        add = k
        count = v
print(f"{add} {count}")

#www.py4e.com/code3/clown.txt