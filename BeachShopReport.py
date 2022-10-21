def order_total(p, q):
    return p * q

# second called function that calculates total for each customer on record

def main():

    grand_total = 0

    print("%13s  %-20s  %5s  %8s  %6s" % ("Customer Name", "Item", "Price", "Quantity", "Total"))
    
# reading makewaves.txt without modifying:

    f = open("makewaves.txt", "r")

# created a loop that processes records from the file, irregardless of number of records

    for line in f:

        name, item, price, quantity = line.split(",")

        price = float(price)
        quantity = float(quantity)
        
        total = order_total(price, quantity)
        
        grand_total += total

# print all information from file, justified and aligned, with currencies formatted to two decimal places

        print("%-13s  %-20s  %5.2f  %8.0f  %6.2f" % (name, item, price, quantity, total))
    
    print("\nToday's Total Sales: $" + str(grand_total))

    f.close()

main()