name = input("\n What is your name? \n")
allowedUsers = ['Jenny','Calvin','Rod']
allowedPassword =['passwordJ','passwordC','passwordR']
import datetime
now = datetime.datetime.now()

if(name in allowedUsers):
    password = input("Your password \n")
    userId = allowedUsers.index(name)
else:
    print('Name is NOT found, please try again')
    
def atm():
        if(password == allowedPassword[userId]):
            print('Welcome %s' % name)
            print('Current date and time is: ')
            print(now.strftime("%Y/%m/%d %H:%M"))
            print('\n These are the available options: ')
            print('1. Withdrawl')
            print('2. Cash Deposit')
            print('3. Complaint')

            selectedOption = int(input("\n Please select an option: "))

            if(selectedOption == 1):
                print('You selected %s' % selectedOption)
                userChoice = (input('\n Enter "W" to withdraw an amount or enter "E" to return to Main Menu: '))
                if(userChoice == "W"):
                    amount = int(input('\n How much would you like withdraw? '))
                    print('\n Amount Withdrawn: %d, Take your Cash' % amount)
                elif(userChoice == "E"):
                    atm()
                    pass
                else:
                    print('Error, Please Enter a "W" or a "E"')
            elif(selectedOption == 2):
                print('You selected %s' % selectedOption)
                userChoice = (input('\n Enter "D" to deposit money into the account or enter "E" to return to Main Menu: '))
                if(userChoice == "D"):
                    amount = int(input('\n How much are you depositing? '))
                    print('\n Current Balance: %d' % amount)
                elif(userChoice == "E"):
                    atm()
                    pass
                else:
                    print('Error, Please Enter a "D" or a "E"')
            elif(selectedOption == 3):
                print('You selected %s' % selectedOption)
                userChoice = (input('\n Enter "C" to enter a complaint or enter "E" to return to Main Menu: '))
                if(userChoice == "C"):
                    issue = (input('\n Whatissue would you like to report? '))
                    print('\n Thank you for contacting us')
                elif(userChoice == "E"):
                    atm()
                    pass
                else:
                    print('Error, Please Enter a "C" or a "E"')
            else:
                print('Invalid option, please try again')                     
        else:
            print('Password is INCORRECT, please try again')
    
atm()