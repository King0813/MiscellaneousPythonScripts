import random
   
# initializing list 
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
# printing original list 
#print ("Original list is : " + str(test_list))
  
# using random.choice() to 
# get a random number 

computerRandomNumber = 0
#print(type(computerRandomNumber))
computerRandomNumber = random.choice(test_list)
#print(type(computerRandomNumber))

choiceFlag = ''
#print(type(choiceFlag))

userNumberChoice = 0
#print(type(userNumberChoice))


# #while choiceFlag == 'Y' or choiceFlag == ''

# while userNumberChoice != computerRandomNumber or choiceFlag != 'N' or choiceFlag != 'n':

#     print(type(computerRandomNumber))
#     userNumberChoice = input("Please select a number between 1 and 10: ")
#     #userNumberChoice = int(userNumberChoice)
#     print(computerRandomNumber)
#     print(type(computerRandomNumber))
#     userNumberChoice = int(userNumberChoice)
#     print(type(userNumberChoice))
#     if userNumberChoice == computerRandomNumber:
#         print("Congratulations you picked the right number!!")
#         choiceFlag = input("Would you like to play again? (Y/N): ")
#     else:
#         if userNumberChoice < computerRandomNumber:
#             print("Sorry that is not the number. The computer's number is higher")
#         else:
#             print("Soory that is no tthe number. Your number is lower")
# # # printing random number
# # #print ("Random selected number is : " + str(computerRandomNumber))


#slice(1, 10, 1)

def guessRandomNumber(tries, start, stop):
    random_number =  random.randrange(start,stop)
    theRange = range(start,stop)
    print("You have the following number of tries to guess: ", random_number)
    while tries != 0:
        for a in theRange:
            if theRange[a] != random_number:
                print("number of tries left: ", tries)
                print("the program is guessing ... ", a)
                tries -= 1
                if tries == 0:
                    print("the program has failed to guess the correct number")
                    return




#guessRandomNumber(5,0,11)
 


def guessRandomNumberLinear(tries, start, stop):
    random_number =  random.randrange(start,stop)
    theRange = range(start,stop)
    print("You have the following number of tries to guess: ", tries)
    print("The number is: ", random_number)
    initialTries = tries

    while tries != 0:
        
        
        
        
     
 
        for i in theRange:
                    
             
             
            if tries == 0:
                print("the program has failed to guess the correct number")
                return
            print("You have the following tries left: ", tries)
            
             
            if tries == initialTries:
                print("number of tries left: ", tries)
                print("the program is guessing ... ", i)
            if i != random_number:
                print("number of tries left: ", tries)
                print("the program is guessing ... ", i)
                tries -= 1
            else:
                print("the program has guessed the correct number")
                return
        
 

#guessRandomNumberLinear(5,0,11)

# this can be coded out
# def binarySearch(item_list,item):
# 	first = 0
# 	last = len(item_list)-1
# 	found = False
# 	while( first<=last and not found):
# 		mid = (first + last)//2
# 		if item_list[mid] == item:
# 			found = True
# 		else:
# 			if item < item_list[mid]:
# 				last = mid - 1
# 			else:
# 				first = mid + 1	
# 	return found
	


def guessRandomNumberBinary(tries, start, stop):
    random_number =  random.randrange(start,stop)
    theRange = range(start,stop)
    print("You have the following number of tries to guess: ", tries)
    print("The number is: ", random_number)
    initialTries = tries

    item_list = list(range(start, stop))
    #print(item_list)

 
    first = 0
    mid = 0
    
    last = len(item_list)-1
     
    found = False
    
    #while tries != 0:
        
    #print("tries left: ", tries)
    while(first <= last and not found):
        tries -= 1
        if tries == 0:
            print("Your program failed to find the number")
            return
 	     
        mid = (first + last)//2
        print("The program guessed: ", mid)
        if item_list[mid] == random_number:
            print("Found It", random_number)
            found = True
    
        else:
        
            if random_number < (item_list[mid]):
                    
                print("Guessing Lower")

                last = item_list[mid] - 1
               
         
            else:

                print("Guessing Higher")

                first = item_list[mid] + 1

             
    return found


 

guessRandomNumberBinary(5, 0, 100)