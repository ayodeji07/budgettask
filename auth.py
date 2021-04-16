#register
#- first name, last name, email, password
#- Generate account number


#login
#- account number, password


#bank operations

#Initializing the system

import random

database = {}

def init():
    
    print("Welcome to bank CSS")

    haveAccount = int(input("Do you have an account with us: (1) yes (2) no \n"))
    
    if(haveAccount == 1):   
        login()
    elif(haveAccount == 2):  
        register()
    else:
        print("Invalid option, please try again")
        init()

def login():
    
    print("********Enter your details to login*********")

    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountNumber,userDetails in database.items():
        if(userDetails[3] == password):
            bankOperation(userDetails)
        else:
             print('Invalid account or password')
             login()
    

def register():
    
   print("********Register********")  
   email = input("What is your email? \n")
   first_name = input("What is your first name? \n")
   last_name = input("What is your last name? \n")
   password = input("Create your password? \n")

   accountNumber = generateAccountNumber()

   database[accountNumber] = [first_name, last_name, email, password]

   print("Your account has been created")
   print('Your account number is %d' % accountNumber)
   
   login()
   


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    optionSelected = int(input('What operation would you like to perform? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if(optionSelected == 1):
        depositOperation()
    elif(optionSelected == 2):
        withdrawalOperation()
    elif(optionSelected == 3):
        logout()
    elif(optionSelected == 4):
        exit()
    else:
        print('Invalid Option selected')
        bankOperation(user)

    
def depositOperation():
    print('Deposit')

def withdrawalOperation():
    print('Withdrawal')

def logout():
    login()


                           
def generateAccountNumber():
    
    return random.randrange(0000000000,9999999999)



############ Actual Banking Operations ########

init()




    
