kind_of_input = input()
temperature = input()
if kind_of_input == "Celsius to Fahrenheit":
    print(round((int(temperature)*9/5) + 32 ,4))
elif kind_of_input == "Fahrenheit to Celsius":
    print(round((int(temperature)-32)*5/9,4))
