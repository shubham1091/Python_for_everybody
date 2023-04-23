# 5.1 write a program which repeatedly reads number until the user enters "done" 
# Once "done" is entered, print out the total count and average of the numbers
# if the user enteres anything other than number, detect their mistake useing
# try and except and print an error message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

count = 0
sum = 0

while True:
    value = input("Enter a number: ")
    if value == "done":
            break
    try:
        num = float(value)
    except:
        print("Invalid input")
        continue
    count += 1
    sum = sum + num
print(sum,count,sum/count)
