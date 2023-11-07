def main(temp):
    
    if temp < 0:
        return "Very Cold"
    if temp >= 1 and temp <=10:
        return "Freezing"
    if temp >= 11 and temp <= 20:
        return "Cold"
    if temp >= 21 and temp <= 30:
        return "Normal"
    if temp >= 31 and temp <= 40:
        return "Hot"
    if temp >40:
        return "Very Hot"
print(main(14))
print(main(2))