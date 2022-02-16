def login(database, username, password):
  
    for key in database:
        
        if username in database.values() and password in database.values():
            print("Hello", username)
            print("Welcome back ", username)
            return username
           

        elif username in database.values() and password not in database.values():
            print("ERROR!!: PLEASE REENTER PASSWORD")
            return username
        else:
            print("ERROR!! Usernname not found")
            return username



def register(database,username):
    
    
     

    number = 0

    for key in database:
        if username in database.values():
            print(username, "User Already Registered")
            
            return False
        else:
            
            return True


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


    