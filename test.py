def getTax(amount, rate = .05) : 
    tax = amount * rate 
 
def main() : 
    subtotal, TAX_RATE = 100, .06 
    taxDue = getTax(subtotal, TAX_RATE) 
    print(taxDue) 
 
main()