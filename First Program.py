c=0
sale = 0
quanitiy = 0
total_received = 0
change_received = 0

print("Fruta Raspada")
        

print("1.Shaved Ice - 5", "\n2.Smoothie - 6", "\n3.ice cream - 4", "\n4.Aguas de fruta(fruit drinks) - 2","\n5.End of order", "\n6.Exit")

while (1):

            c = int(input("Please enter your Menu Item Number or 5 to end order: "))

            if (c == 1):

                quantity = int(input("Enter the quantity: "))
                sale = sale + 5 * quantity

            elif (c == 2):
                quantity = int(input("Enter the quantity: ")) 
                sale = sale + 6 * quantity

            elif (c == 3):
                quantity = int(input("Enter the quantity: "))
                sale = sale + 3 * quantity

            elif (c == 4):
                quantity = int(input("Enter the quantity: "))
                sale = sale + 2 * quantity

            elif (c == 5):
                print("Total Sale:", sale)
                if (sale > 0):
                    total_received = int(input("Total payment received: "))
                    print("Change: ", total_received - sale)
                    print("*****Thank You Come Again!!!*****")
                    quit()
            elif (c == 6):
                    quit()
            else:
                    print("Please enter a valid option (1-5): ")
    
