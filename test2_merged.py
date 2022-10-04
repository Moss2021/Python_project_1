import inquirer
from datetime import date 

#Fruits in Ascii:
apple_ascii = '''
           .:'
         __ :'__
      .'`  `-'  ``.
     :             :
     :             :
      :           :
       `.__.-.__.'

'''

banana_ascii = '''

 /`-.__                                 /\
 `. .  ~~--..__                   __..-' ,'
   `.`-.._     ~~---...___...---~~  _,~,/
     `-._ ~--..__             __..-~ _-~
         ~~-..__ ~~--.....--~~   _.-~
                ~~--...___...--~~
'''


pear_ascii = '''

                     /)
                  ,.//,
                /` `'` `\
               :         :
              :           :
             :             :
            :               :
           :                 ;
          :                   :
          ;                   ;
          ;                   ;
          :                   :
           \                 /
            `._,.='``'-.,_,.`
              '-._  ~  _.-'
                  `''`
'''
#Date
today = date.today()
print("Today's date:", today)
print(" \n")
print("Welcome to Fruta Raspada!\n")
name = input("What is your name? ")
print("Hello " + name + ", are you ready to order a fruit flavor ? \n")
#Ask user for name and fruit choice
userReply = input("Enter yes or no: \n").lower()
     
if userReply == "no":
    print(" \n")
    print("No worries! Please come back when you are hungry! \n")
    quit()
while userReply == "yes":    
                    questions = [
                        inquirer.List('fruit',
                                      message="Please select a fruit from below: ",
                                      choices=['apple', 'banana', 'pear']
                                      ),
                    ]
                    answers = inquirer.prompt(questions)
                    print("Here you go! Enjoy")
                    if (answers['fruit'] == "apple"):
                        print(apple_ascii)
                    if (answers['fruit'] == "banana"):
                        print(banana_ascii)
                    if (answers['fruit'] == "pear"):
                        print(pear_ascii)
                    
                    print(answers)
                    print(" \n")
                    print(name + " would you like another fruit flavor?\n")
                    userReply = input("Enter yes or no: ").lower()
                
print(" \n")  
print("Ok! Please choose what you want to do with the fruit! (type 1 to 4)\n(type 5 for PAYMENT or type 6 to EXIT )")
print(" \n")   

c=0
sale = 0
quanitiy = 0
total_received = 0
change_received = 0

print("1.Shaved Ice - $5", "\n2.Smoothie - $6", "\n3.Ice Cream - $4", "\n4.Aguas de fruta(fruit drinks) - $2","\n5.Payment", "\n6.Exit \n")

while (1):

            c = int(input("Please type the number of your choice: "))

            if (c == 1):

                quantity = int(input("Enter the quantity: "))
                sale = sale + 5 * quantity

            elif (c == 2):
                quantity = int(input("Enter the quantity: ")) 
                sale = sale + 6 * quantity

            elif (c == 3):
                quantity = int(input("Enter the quantity: "))
                sale = sale + 4 * quantity

            elif (c == 4):
                quantity = int(input("Enter the quantity: "))
                sale = sale + 2 * quantity

            elif (c == 5):
                print("Total Sale:", sale)
                if (sale > 0):
                    total_received = int(input("Total payment received: "))
                    print("Your change: ", total_received - sale)
                    print("*****Thank You Come Again!!!*****")
                    quit()
            elif (c == 6):
                    quit()
            else:
                    print("Please enter a valid option (1-5): ")
    

        



