#Initialize values of variables:
menu_item=0
sale = 0
quantity = 0
total_received = 0
change_received = 0

print("1.Shaved Ice - $5", "\n2.Smoothie - $6", "\n3.Ice Cream - $4", "\n4.Aguas de fruta(fruit drinks) - $2","\n5.Payment", "\n6.Exit \n")

#this loop continues while the condition is true
while (1):
            #fail-safe in case invalid choice is input
            try:          
            #Menu's choice & quantity determine the sale amount
                menu_item = int(input("Please type the number of your choice: "))
            except:
                menu_item = int(input("Please type the number of your choice: ")) 
                            
            if (menu_item == 1):
                quantity = int(input("Enter the quantity: "))  
                sale = sale + 5 * quantity

            elif (menu_item == 2):
                quantity = int(input("Enter the quantity: ")) 
                sale = sale + 6 * quantity

            elif (menu_item == 3):
                quantity = int(input("Enter the quantity: "))
                sale = sale + 4 * quantity

            elif (menu_item == 4):
                quantity = int(input("Enter the quantity: "))
                sale = sale + 2 * quantity
                      
            #when customer is finished ordering, the total sale is calculated
            elif (menu_item == 5):
                print("Total Sale:", sale)
                if (sale > 0):
                    #Customer is prompted to input amount they will use to pay sale
                    total_received = int(input("Total payment received: "))
                    #Calculate change
                    print("Your change: ", total_received - sale)
                    print("*****Thank You Come Again!!!*****")
                    quit()
                      
            #when customer wants to end order
            elif (menu_item == 6):
                print("Have a nice day!")
                quit()
           
            #if customer selects number outside of range, he is prompted to type valid option
            else:
                print("Please enter a valid option (1-5): ")
