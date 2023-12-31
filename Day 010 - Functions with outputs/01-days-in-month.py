def is_leap(year):
  """
    Check if a given year is a leap year or not.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    """
    Calculate the number of days in a given month of a given year.

    Args:
        year (int): The year.
        month (int): The month (1 to 12).

    Returns:
        int: The number of days in the specified month and year.
    """
    month_days_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        return month_days_leap[month-1]
    else:
        return month_days_non_leap[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



