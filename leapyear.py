year = int(input("Enter the year: "))

if year % 400 == 0:
    print("This is a leap year:", year)

elif year % 100 == 0:
    print("This is not a leap year:", year)

elif year % 4 == 0:
    print("This is a leap year:", year)

else:
    print("This is not a leap year:", year)



year = int(input("Enter the year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")