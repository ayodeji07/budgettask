budget_food = 0 
budget_clothing = 0
budget_entertainment = 0

balance = [budget_food, budget_clothing, budget_entertainment]
balance[0] += budget_food
balance[1] += budget_clothing
balance[2] += budget_entertainment



def init():
    print('************WELCOME*************')
    action = int(input('what would you like to do. (1) Deposit (2) Withdraw (3) Transfer (4) Check Balance \n'))

    if(action == 1):
        budget_1.deposit()
    elif(action == 2):
        budget_1.withdrawal()
    elif(action == 3):
        budget_1.Transfer()
    elif(action == 4):
        budget_1.checkBalance()
    else:
        print('Invalid option selected')
        init()




class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        
    def deposit(self):
        print('**********DEPOSIT**********')
        budget_food = int(input('Set budget deposit for food \n'))
        budget_clothing = int(input('Set budget deposit for clothing \n'))
        budget_entertainment = int(input('Set budget deposit for entertainment \n'))

        print(f'You have deposited {self.food} for food, {self.clothing} for clothing, {self.entertainment} for entertainment')


    def checkBalance(self):

        print('*********CHECK AVAILABLE BALANCE***********')
              
        selectedOption = int(input('Select category. (1) Food (2) Clothing (3) Entertainment \n'))
        if(selectedOption == 1):
            print('Your balance is %d' % balance[0])
        elif(selectedOption == 2):
            print('Your balance is %d' % balance[1])
        elif(selectedOption == 3):
            print('Your balance is %d' % balance[2])
        else:
            print('Invalid option selected')
            budget_1.checkBalance()
            


    def withdrawal(self):

        print('**********WITHDRAWAL***********')
              
        selectedOption = int(input('Select category to withdraw from. (1) Food (2) Clothing (3) Entertainment \n'))
        if(selectedOption == 1):
            
            amountToWithdraw = int(input('Enter amount to withdraw: \n'))
            balance[0] -= amountToWithdraw
            print('You have withdrawn %d from your budget, your balance is %d' % (amountToWithdraw, balance[0]))
            
        elif(selectedOption == 2):
            
            amountToWithdraw = int(input('Enter amount to withdraw: \n'))
            balance[1] -= amountToWithdraw
            print('You have withdrawn %d from your budget, your balance is %d' % (amountToWithdraw, balance[0]))
            
        elif(selectedOption == 3):
            
            amountToWithdraw = int(input('Enter amount to withdraw: \n'))
            balance[0] -= amountToWithdraw
            print('You have withdrawn %d from your budget, your balance is %d' % (amountToWithdraw, balance[0]))
        else:
            print('Invalid option selected')
            budget_1.withdrawal()
            

    def Transfer(self):

        print('**********TRANSFER FUNDS***********')
        selectedOption_1 = int(input('Select category to transfer from. (1) Food (2) Clothing (3) Entertainment \n'))
        selectedOption_2 = int(input('Select category to transfer to. (1) Food (2) Clothing (3) Entertainment \n'))

        if(selectedOption_1 == 1 and selectedOption_2 == 2):
            
            amountTransfer = int(input('Enter amount to transfer: \n'))
            balance[0] -= amountTransfer
            balance[1] += amountTransfer
            
            print('You have transferred %d to clothing category, your new balance is %d for food and %d for clothing' % (amountTransfer, balance[0], balance[1]))
        elif(selectedOption_1 == 1 and selectedOption_2 == 3):            

            amountTransfer = int(input('Enter amount to transfer: \n'))
            balance[0] -= amountTransfer
            balance[2] += amountTransfer
            
            print('You have transferred %d to entertainment category, your new balance is %d for food and %d for entertainment' % (amountTransfer, balance[0], balance[2]))

        elif(selectedOption_1 == 2 and selectedOption_2 == 1):            
            amountTransfer = int(input('Enter amount to transfer: \n'))
            balance[1] -= amountTransfer
            balance[0] += amountTransfer
            
            print('You have transferred %d to food category, your new balance is %d for clothing and %d for food' % (amountTransfer, balance[1], balance[1]))


        elif(selectedOption_1 == 2 and selectedOption_2 == 3):            

            amountTransfer = int(input('Enter amount to transfer: \n'))
            balance[1] -= amountTransfer
            balance[2] += amountTransfer
            
            print('You have transferred %d to entertainment category, your new balance is %d for clothing and %d for entertainment' % (amountTransfer, balance[1], balance[2]))

        elif(selectedOption_1 == 3 and selectedOption_2 == 1):            

            amountTransfer = int(input('Enter amount to transfer: \n'))
            balance[2] -= amountTransfer
            balance[0] += amountTransfer
            
            print('You have transferred %d to food category, your new balance is %d for entertainment and %d for food' % (amountTransfer, balance[2], balance[0]))

        
        elif(selectedOption_1 == 1 and selectedOption_2 == 3):            

            amountTransfer = int(input('Enter amount to transfer: \n'))
            balance[2] -= amountTransfer
            balance[1] += amountTransfer
            
            print('You have transferred %d to clothing category, your new balance is %d for entertainment and %d for clothing' % (amountTransfer, balance[2], balance[1]))

        else:
            print('Invalid Option selected')
            budget_1.Transfer()

                       



budget_1 = Budget(budget_food, budget_clothing, budget_entertainment)
init()

        


   


            

