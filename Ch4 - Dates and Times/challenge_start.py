# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar
def countdays(theyear, themonth, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

print("--Day counter program--\n")

run = True
while (run):
    try:
        print("The day I want to count is: ")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or Q to quit")

        theday = input("? ")
        if theday=="Q":
            run=False
            break
        day = int(theday)
        yr = int(input("Enter a year: "))
        mon=int(input("Enter a month: "))

        result = countdays(yr,mon,day)
        print("There are " + result + "days in requested month and year")
    except Exception as e:
        print(e)
        print("Entry not valid")