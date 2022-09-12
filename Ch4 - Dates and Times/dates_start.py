#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
    # DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()

    print(today)
    # TODO: print out the date's individual components
    print(today.day, today.month, today.year)

    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] #create a list of assigned days, as the weekday function returns a number from 0 to 6
    print(days[today.weekday()])

    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    dateToday=datetime.now()
    print(dateToday)

    
    # TODO: Get the current time
    #need to get time portion from the previous result
    t = datetime.time(datetime.now()) #get the time from datetime.now method
    print(t)

  
if __name__ == "__main__":
    main()
  