import TerminalManager as term
import Userbase as base
import Transaction as trans
#Main, pretty self explanatory

#Handle the actual menu
def main_menu():

    print('1. Log In')
    print('2. Sign Up')
    print('3. Exit')
    choice = input('Please make your selection: ')

    if choice == "1":

        term.clear()

        name = input('Please enter your name: ')
        key = input('Please enter your private key: ')

        #If we can't varify you, go back to the menu
        if not base.verify_key(name, key):
            term.clear()
            term.print_error('Cannot verify user ' + name)
            main_menu()

        term.clear()
        user_menu(name, key)

    elif choice == "2":
        term.clear()
        term.print_header('Thank you for choosing PicoCoin as your wallet, let\'s get started!')
        base.create_user()
        main_menu()
    elif choice == "3":
        term.clear()
        term.print_header('Thank you for choosing PicoCoin! Have a great day!')
    else:
        term.clear()
        term.print_error("Invalid selection, please try again")
        main_menu()
       
#Login babyyyyyy
def user_menu(name: str, key: str):

    balance = base.get_balance(name, key)

    term.print_header('Welcome back, ' + name + '!\n')
    print('Current balance: ', end='')
    
    #No money? Heh, you get the red text, buddy
    if balance > 0:
        term.print_success(str(balance) + 'PC')
    else:
        term.print_error(str(balance) + 'PC')

    print('Public key: ', end='')
    term.print_key(base._create_key(name, key) + '\n')

    print('1. Deposit')
    print('2. Withdraw')
    print('3. Transfer')
    print('4. Transaction History')
    print('5. Delete Account')
    print('6. Log Out')

    choice = input('Please enter your choice: ')

    if choice == '1':
        term.clear()
        trans.deposit(name, key)
        user_menu(name, key)
    elif choice == '2':
        term.clear()
        trans.withdraw(name, key)
        user_menu(name, key)
    elif choice == '3':
        term.clear()
        trans.transfer(name, key)
        user_menu(name, key)
    elif choice == '4':
        term.clear()
        trans.get_history(name, key)
        user_menu(name, key)
    elif choice == '5':
        term.clear()
        base.remove_user(name)
        main_menu()
    elif choice == '6':
        term.clear()
        term.print_header('See you next time, ' + name + '!')
        main_menu()
    else:
        term.clear()
        term.print_error('Invalid input!')
        user_menu(name, key)

#Main method
if __name__ == '__main__':

    term.clear()
    term.print_header("Welcome to the PicoCoin terminal!")
    main_menu()