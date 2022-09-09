# Joshua Beld - CIT 144: Python - Programming Project 1
startTemp = input("Enter numeric temperature value to convert: ")
endFormat = input("Convert to (C) Celsius or (F) Farenheit? ")

if endFormat == "C" or endFormat == "c":
    degC = (float(startTemp) - 32) / 1.8
    print (str(startTemp) + " degrees Farenheit is equal to " + str(degC) + " degrees Celsius")
elif endFormat == "F" or endFormat == "f":
    degF = (1.8 * float(startTemp)) + 32
    print(str(startTemp) + " degrees Celsius is equal to " + str(degF) + " degrees Farenheit")
else:
    print("You did not enter an F or C, goodbye.")