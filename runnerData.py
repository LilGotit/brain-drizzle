import csv

def readData():
    fields = ("Name", "Boston", "Chicago", "New York")
    file = open("runners1.txt", "r")
    data = []
    dReader = csv.DictReader(file, fieldnames=fields, delimiter=",")

    for row in dReader:
        data.append(row)

    file.close()
    return data

def displayAll(data):
    formatString = "%-8s %-10s %-10s %-10s"
    print(formatString % ("Name", "Boston", "Chicago", "New York"))

    for runner in data:
        print("%-8s %-10s %-10s %-10s" % (runner["Name"], runner["Boston"], runner["Chicago"], runner["New York"]))

def displayRunner(data):
    formatString = "%-8s %-10s"
    exact = input("Enter a runner: ")

    for runner in data:
        if runner["Name"] == exact:
            print(formatString % ("Name", "Average"))
            print(formatString % (runner["Name"], ((int(runner["Boston"]) + int(runner["Chicago"]) + int(runner["New York"]))//3)))
    
def addRunner(data):
    nom = input("Enter runner name: ")
    boston = int(input("Enter time (in minutes) the runner ran the Boston Marathon: "))
    chicago = int(input("Enter time (in minutes) the runner ran the Chicago Marathon: "))
    newYork = int(input("Enter time (in minutes) the runner ran the New York Marathon: "))
    record = {"Name": nom, "Boston": boston, "Chicago": chicago, "New York": newYork}
    data.append(record)
    return data

def saveAndExit(data):
    fields = ("Name", "Boston", "Chicago", "New York")
    file = open("runners1.txt", "w")
    dWriter = csv.DictWriter(file, fieldnames=fields, delimiter=",", lineterminator="\n")
    dWriter.writerows(data)
    
    file.close()

def main():
    runners = readData()

    while True:
        print("""
        Menu options. Choose 1, 2, 3, or 4:
            1. Display all data for all racers
            2. Display a runner's individual race average (in minutes)
            3. Add a new runner and race data
            4. Save & Exit
            
         """)
        
        opt = input("Enter your choice, 1, 2, 3, or 4: ")

        if opt == "1":
            displayAll(runners) 

        elif opt == "2":
            displayRunner(runners)

        elif opt == "3":
            runners = addRunner(runners)

        elif opt == "4":
            print()
            print("Goodbye")
            saveAndExit(runners)
            break

        else:
            print()
            print("Invalid entry, please re-enter your choice")
            print()

main()