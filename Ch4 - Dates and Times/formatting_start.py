#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    now = datetime.now()

    # Times and dates can be formatted using a set of predefined string
    # control codes 

    
    #### Date Formatting ####
    print(now.strftime("%Y"))
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("%Y, %a, %B, %d"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("%X"))

    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("%I"))
    print(now.strftime("%H"))
    print(now.strftime("%p"))
    print(now.strftime("%H %M %S"))

if __name__ == "__main__":
    main()
