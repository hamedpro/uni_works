user_input = input()
temperature = user_input.split(' ')[0]
unit = user_input.split(' ')[1]

if unit == "ft"  or unit == "inch":
    if unit == "ft" : 
        print(str(round((float(temperature)*12*2.54),4)) + " cm")
    elif unit == "inch":
        print(str(round((float(temperature) * 2.54),4)) + " cm")
elif unit == "cm":
    print(str(round((float(temperature) / (2.54)),4)) + " inch")
    print(str(round((float(temperature) / (2.54 * 12)),4)) + " ft")
