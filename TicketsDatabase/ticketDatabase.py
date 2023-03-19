import sqlite3

conn = sqlite3.connect("tickets5.db")
cur = conn.cursor()     

def displayAllTickets():
    sql = "SELECT * FROM tickets"
    cur.execute(sql)

    results = cur.fetchall()

    if results:
        printStuff(results)
    else:
        print("No data found")

    print()

def addTicket():
    actual_speed = int(input("Enter actual speed: "))
    posted_speed = int(input("Enter posted speed: "))
    age = int(input("Enter age of offender: "))
    violator_sex = str(input("Enter sex of offender: "))

    data = (None, actual_speed, posted_speed, age, violator_sex)
    sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?)"

    cur.execute(sql, data)
    conn.commit()   
    
def displayTicketsByOffender():
    violator_sex = input("Enter sex of offender: ")
    data = (violator_sex, )

    sql = "SELECT * FROM tickets WHERE violator_sex = ?"
    
    cur.execute(sql, data)
    results = cur.fetchall()

    if results:
        printStuff(results)
    else:
        print("Name not found")
        print()

def printStuff(data):
    print("%-10s %-12s %-10s %-5s %-12s " % ("ticketID", "Posted MPH", "MPH Over", "Age", "Violator Sex"))

    for row in data:
        over = row[1] - row[2]
            
        print(" %-10d %-12d %-10d %-5d %-12s " % (row[0], row[1], over, row[3], row[4]))     
     
    print()

def main():
    
    while True:
    
        print(""" 
            Menu options. Choose 1, 2, 3, or 4:  
            
            1. Display all Tickets
            2. Add a Ticket
            3. Filter by Offender Sex
            4. Save & Exit

        """) 

        opt = input("Enter your choice, 1, 2, 3, or 4: ") 

        if opt == "1": 
            displayAllTickets()
            
        elif opt == "2": 
            addTicket()

        elif opt == "3":  
            displayTicketsByOffender()
            
        elif opt == "4":
            print() 
            print("Goodbye") 
      
            if conn:
                conn.close
            break

        else: 
            print("Invalid entry, please re-enter your choice") 
            print()
            
main()