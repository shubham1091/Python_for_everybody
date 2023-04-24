fname = input("Enter File: ")

if len(fname) < 1:
    fname = "../Data/clown.txt"

hand = open(fname, "r")
di = dict()

for line in hand:
    line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

# now wo want to find the most common word
largest = -1
word  = None
for k,v in di.items():
    if v > largest:
        largest = v
        word = k

print("'",word,"' appeared", largest, "times")
print(w)
print(line)