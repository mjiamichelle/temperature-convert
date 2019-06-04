temperature = int(input("what's the temperature?"))
unit = input("do you want to convert to F or C?")

if unit == "F":
    print(temperature*9/5+32)
elif unit == "C":
    print((temperature-32)*5/9)
else:
    print("you are stupid!")
