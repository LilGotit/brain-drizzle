import csv
import json

def readData():
    data = []
    try:
        with open("runners.txt", "r") as file:
            data = json.load(file)
    except IOError:
        print("Creating empty dictionary...")
    return data

def displayAll(data):
    if len(data) == 0:
        print("No data has been entered")
        return
    
    print()
    print("%-10s %012s %4s" % ("State", "Capital", "Year of Statehood"))
    for state in data:
        print("%-10s %-12s %4s" % (state['name'], state['capital'], state['year']))

    print()

def displayRunner(data):
    if len(data) == 0:
        print("No data has been entered")
        return
    
    print()
    print("%-10s %012s %4s" % ("State", "Capital", "Year of Statehood"))
    for state in data:
        print("%-10s %-12s %4s" % (state['name'], state['capital'], state['year']))

    print()

def addRunner(data):
    d = {}
    d['name'] = input("Enter state name: ")
    d['capital'] = input("Enter state capital: ")
    d['year'] = input("Enter year of statehood: ")

    data.append(d)
    return data

def saveAndExit(data):
    with open("runners.txt", "w") as file:
        json.dump(data, file)

def reader():
    csv.DictReader()

def main():
    states = readData()

    while True:
        print("""
        Menu options. Choose 1, 2, or 3
            1. Enter a new state, capital, and year of statehood
            2. Display capital data
            3. Exit
            
         """)
        
        opt = input("Enter your choice, 1, 2, or 3: ")

        if opt == "1":
            states = addRunner(states)

        elif opt == "2":
            displayRunner(states)

        elif opt == "3":
            print()
            print("Goodbye")
            saveAndExit(states)
            break

        else:
            print("Invalid entry, please re-enter your choice")
            print()

main()