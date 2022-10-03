#Fruits in Ascii:
#Testing of comment
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

#Declare functions:

def choose_fruit():
    print("Please select the fruit you want from the list provided! ")
    print("Which fruit do you want? ")

#Ask user for name and fruit choice
name = input("What is your name? ")
print("Hello " + name + ", would you like a fruit? ")
userReply = input("Enter yes or no: ")
#YESSSSSSSSSSSSSSSS
if userReply == "yes":
    print("Please select the fruit you want from below: ")
    fruitDict = {}
    option = []
    fruitList = ["apple", "banana", "pear"]
    fruitascii = [apple_ascii, banana_ascii, pear_ascii]
    for index in range(len(fruitList)): #len function returns the number of items in an object
        opt = str(index + 1)
        option.append(opt)
        fruitDict[opt] = fruitascii[index]
        print(opt + ". " + fruitList[index])
       
 ############################   
    answer = input("Chosen fruit> ").lower()
    #if answer != fruit_indx:
        #choose_fruit()
        #answer = input("Chosen fruit> ").lower()  
    
    fruit_indx = fruitList.index(answer) #fruit list
    fruit_indx = str(fruit_indx + 1)
    
    print(option)
    for op in option:
        if fruit_indx == op:
            print("Here you go! ")
            print(fruitDict[op])
            
        #else:
            #fruit_indx != fruitList.index(answer)
            #choose_fruit()
        #answer = input("Chosen fruit> ").lower()   
           
#if user says "No" to fruit:        
else:
    print("No worries! " + name + ", please come back when you are hungry! ")
    
print("Thank you for playing")


        

