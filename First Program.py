:        sale.r = r
        
    def foods(sale):

        print("Menu for Tienda de Raspadas")
        
        print("1.Shaved Ice - 5", "\n2.Smoothie - 6", "\n3.Lemonade - 3", "\n4.Soda - 2","\n5.End of order", "\n6.Exit")

        while (1):

            c = int(input("Please enter your Menu Item Number or 5 to end order: "))

            if (c == 1):
                quantity = int(input("Enter the quantity: "))
                sale.r = sale.r + 5 * quantity

            elif (c == 2):
                quantity = int(input("Enter the quantity: ")) 
                sale.r = sale.r + 6 * quantity

            elif (c == 3):
                quantity = int(input("Enter the quantity: "))
                sale.r = sale.r + 3 * quantity

            elif (c == 4):
                quantity = int(input("Enter the quantity: "))
                sale.r = sale.r + 2 * quantity

            elif (c == 5):
                print("Total Sale:", sale.r)
                if (sale.r > 0):
                    received = int(input("Total payment received: "))
                    print("Change: ", received - sale.r)
                    print("*****Thank You Come Again!!!*****")
                    quit()
            elif (c == 6):
                    quit()
            else:
                    print("Please enter a valid option: ")
    
def main():
    a = cashiersystem()

    while (1):

            a.foods()

main()