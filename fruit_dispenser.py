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
print("Welcome to the FRUIT Dispenser!\n")
today = date.today()
print("Today's date:", today)
print(" \n")
#Ask user for name and fruit choice
name = input("What is your name? \n")
print("Hello " + name + ", would you like a fruit? \n")
userReply = input("Enter yes or no: \n").lower()


#YESSSSSSSSSSSSSSSS

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
                    print(name + " would you like another fruit?\n")
                    userReply = input("Enter yes or no: \n").lower()
    

#Answer NO:       
else:
    print(" \n")
    print("No worries! Please come back when you are hungry! \n")
    print("Thank you for playing " + name + " !!!")




