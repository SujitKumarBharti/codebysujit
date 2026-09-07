year = int(input("Enter a year: "))      # Read the year

if year % 400 == 0:                      # Check years exactly divisible by 400
    leap_year = True                     # Mark the year as a leap year
elif year % 4 == 0 and year % 100 != 0:  # Check the other leap year rule
    leap_year = True                     # Mark the year as a leap year
else:
    leap_year = False                    # Mark the year as a normal year

if leap_year:                            # Check the final result
    print("Leap year")                   # Display leap year
else:
    print("Not a leap year")             # Display non-leap year
