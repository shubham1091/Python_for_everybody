import re

fname = input("Enter the name:  ")

if len(fname)<1:
    fname = "../Data/regex_sum_42.txt"

try:
    fhand = open(fname, "r")
except:
    print("File not found")
    quit()

sum = 0
for line in fhand:
    tmp = re.findall("[0-9]+", line)
    if len(tmp) < 1:
        continue
    for i in tmp:
        sum += int(i)
fhand.close()

print(sum)