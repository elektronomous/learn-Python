"""
In the starting code, you'll find the solution from the LeapYear challenge. First,
convert this function is_leap() so that instead of printing "Leap Year." or "Not a
Leap Year." it should return True if it is a leap year and return False if it is
not a leap year.

You're then going to create a function called days_in_month() which will take a year 
and a month as inputs, e.g.:

    days_in_month(year=2022, month=2)
    
And it will use this information to work out the number of days in the month, then
return that as the output e.g.:

    28

The List Month_days contains the number of days in a month from January to December
for a non-leap year. A leap year has 29 days in February:
"""

def is_leap(year:int):
    """Take a year and return True if it's a leap year.
    Otherwise False"""
    if not (year % 4) and (year % 100):
        return True;
    elif not (year % 400):
        return True;
    else: 
        return False;

def days_in_month(year=2022, month=2):
    """Take a year and a month and format it to return the days
    of the year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    
    if is_leap(year) and month == 2:
        return 29;              # because in leap year, only february has 29 days.
    else:
        if month >= 0 and month < 13:
            return month_days[month-1];
        else:
            return "invalid Month/Year.";

def main():
    year = int(input("Enter a year: "));
    month = int(input("Enter a month: "));
    days = days_in_month(year, month);
    print(f"{days}");

if __name__ == "__main__":
    main();