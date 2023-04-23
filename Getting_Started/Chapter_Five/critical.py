# 5.2 Write a program that repeatedly prompts a user for integer numbers until the 
# user enters 'done'. Once 'done' is entered, print out the largest and smallest of the 
# numbers. If the user enters anything other than a valid number catch it with a 
# try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

def get_val():
    usr_inp = input("Enter :") 

    if usr_inp == 'done':
        return usr_inp
    try:
        val = int(usr_inp)
    except:
        val = None
        print("Invalid input")
    
    return val

sm = None
lg = None

while(True):
    inp = get_val()
    if inp is None:
        continue
    elif inp == 'done':
        break
    else:
        if lg is None:
            lg = inp
        if sm is None:
            sm = inp
        if inp > lg:
            lg = inp
        if inp < sm:
            sm = inp
print("Maximum is",lg)
print("Minimum is",sm)