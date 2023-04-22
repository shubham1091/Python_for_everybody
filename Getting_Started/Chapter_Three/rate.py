# 3.1 Write a program to prompt the user for hours 
# and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 
# times the hourly rate for all hours worked above 40 
# hours. Use 45 hours and a rate of 10.50 per hour to 
# test the program (the pay should be 498.75). You should 
# use input to read a string and float() to convert the 
# string to a number. Do not worry about error checking 
# the user input - assume the user types numbers properly.

usr_input = input("Enter Hours: ")
try:
    hrs= float(usr_input)
except:
    hrs=0
usr_input = input("Enter Rate: ")
try:
    rts = float(usr_input)
except:
    rts = 0

amt_pay = 0

if hrs > 40:
    gros = hrs-40
    grat = rts * 1.5
    basic_pay = 40 * rts
    gpay = gros * grat
    amt_pay = basic_pay+gpay
else:
    amt_pay = hrs * rts
print (amt_pay)