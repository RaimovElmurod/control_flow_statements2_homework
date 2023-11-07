def main(number):
   
    if number < 0:
        return "Monday"
    if number >= 1 and number <=2:
        return "Tuesday"
    if number >= 2 and number <=3:
        return "Wednesday"
    if number >= 3 and number <=4:
        return "Thursday"
    if number >= 4 and number <=5:
        return "Friday"
    if number >= 5 and number <=6:
        return "Saturday"
    if number >= 6 and number <=7:
        return "Sunday"
print(main(2))
print(main(6))