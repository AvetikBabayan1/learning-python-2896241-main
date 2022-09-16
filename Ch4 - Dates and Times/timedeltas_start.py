#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#
#
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
#
# # TODO: construct a basic timedelta and print it
# print(timedelta(days=3, hours = 4, minutes=6, seconds=10))
#
# # TODO: print today's date
now = datetime.now()
# print(now)
# # TODO: print today's date one year from now
# print(str(now+timedelta(days=365)))
#
# # TODO: create a timedelta that uses more than one argument
# print(str(now+timedelta(days=3, minutes=24)))
#
# # TODO: calculate the date 1 week ago, formatted as a string
# print(str(now-timedelta(weeks=1)))

### How many days until April Fools' Day?
today=date.today()
afd=date(today.year, 4, 1)
# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd <today:
    afd=afd.replace(today.year+1)

# TODO: Now calculate the amount of time until April Fool's Day  
print(afd-today)
