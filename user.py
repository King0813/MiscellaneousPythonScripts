def login(database, username, password):
     
    attempts = 0
    remainingAttempts = 2
    correctPassword = 0
       
    for key in database:
        
        if username in database.values() and password in database.values():
            print("You are logged in as: ", username)
            
            return 1
           

        elif username in database.values() and password not in database.values():
             
            password = input("ERROR!!: PLEASE REENTER PASSWORD: ")
            while attempts <=2:
                                
                for key in database:

                    if password in database.values():
                        attempts = 2
                        return 1
                    elif password not in database.values():     
                        password = input("ERROR!!: PLEASE REENTER PASSWORD: ")
                        attempts +=1
                        if attempts >= 2:
                            print("You have exceeded login attempts!")
                            return 3
             
                    
        elif username not in database.values():
            print("ERROR!! Usernname not found")
            #print("not registered 2: ", username)
            #username = "c"
     
            return 3



def register(database,username):
    
    
     

    number = 0

    for key in database:
        if username in database.values():
            print(username, "User Already Registered")
            
            return 1
        else:
            
            return 2


def donate(username):     

    donation_amt = input("Enter amount to donate: ")   
    donation_amt = float(donation_amt)

    donation = username, "donated", donation_amt
    print("Thank you for your donation")
    print(username, "donated $", donation_amt)
     
    return donation_amt

def showDonations(donation):
    print("-- All Donations ---")
    if donation == 0:
        print("Currently, there are no donations")
    else:
        print("There was a donation of: ", donation)


    