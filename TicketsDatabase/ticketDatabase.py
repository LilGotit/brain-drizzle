import sqlite3

conn = sqlite3.connect("tickets.db")
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

def addTicket():                         # add a new ticket
    actual_speed = int(input("Enter actual speed: "))
    posted_speed = int(input("Enter posted speed: "))
    age = int(input("Enter age of offender: "))
    violator_sex = str(input("Enter sex of offender: "))

    data = (None, actual_speed, posted_speed, age, violator_sex)
    sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?)"

    cur.execute(sql, data)   # add the record, save changes
    conn.commit()            

def displayTicketsByOffender():
    name = input("Enter sex of offender: ")   # input the user's name. we are assuming each name is unique
    data = (name, )                     # this is a singleton tuple; note the comma and a blank

    sql = "SELECT * FROM travel WHERE name = ?"  # the WHERE clause allows specifying a filter
    
    cur.execute(sql, data)
    results = cur.fetchall()       # If name in table, fetchall() returns all trips with that name  

    if results:
        printStuff(results)        # if records exists, then print then
    else:
        print('Name not found')    # otherwise, no match...
        print()
        
def printStuff(data):    # helper function, just prints whatever was selected
    print(" %-10s %-8s %-15s %-4s " % ('tripID', 'Name', 'Destination', 'MGP'))  # headings

    for row in data:         # row[0] is the id, row[3] is miles, row[4] is gallons
        if row[4] != 0:
            mpg = row[3] / row[4]   # calculate mpg, avoid division by 0
        else:
            mpg = 0
            
        print(" %-10d %-8s %-15s %2.1f " % (row[0], row[1], row[2], mpg))     
     
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