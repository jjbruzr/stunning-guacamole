age = int(input("How old are you?\n"))

decades = age // 10
years = age % 10

if years == 1:
    print("You are " + str(decades) + " decades and " + str(years) + " year old.")
elif years > 1:
    print("You are " + str(decades) + " decades and " + str(years) + " years old.")