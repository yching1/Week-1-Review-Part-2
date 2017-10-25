for tempConversions in range(3):
    inputFahrenheitString = input ("Enter your temperature in F: ")
    tempInF = float(inputFahrenheitString)
    tempInC = round(((tempInF - 32) * 5/9),1)
    print("The temperature in C is", tempInC, "degrees")