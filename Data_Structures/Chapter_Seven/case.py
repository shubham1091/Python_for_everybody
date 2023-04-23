
# 7.1 Write a program that prompts for a file name, then opens that file 
# and reads through the file, and print the contents of the file in upper 
# case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

fname = input("Enter file name: ")
# ../Data/words.txt
try:
    fh = open(fname, 'r')
except:
    print("File not found")
    quit()

for line in fh:
    line=line.rstrip()
    print(line.upper())