import TerminalManager as term
import Userbase as base
import Transaction as trans
#Main, pretty self explanatory

#Handle the actual menu
def main_menu():

    menu = ('1. Log In\n' + 
            '2. Sign Up\n' + 
            '3. Exit')

    term.print_menu(menu, 'Main')

    choice = input('Please make your selection: ')

    match choice:
        case "1":

            term.clear()

            name = input('Please enter your name: ')
            key = input('Please enter your private key: ')

            #If we can't varify you, go back to the menu
            if not base.verify_key(name, key):
                term.clear()
                term.print_error('Cannot verify user ' + name + '.')
                main_menu()

            term.clear()
            user_menu(name, key)

        case "2":
            term.clear()
            term.print_header('Thank you for choosing PicoCoin as your wallet, let\'s get started!')
            base.create_user()
            main_menu()
        case "3":
            term.clear()
            term.print_header('Thank you for choosing PicoCoin! Have a great day!')
        case _:
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

    menu = ('1. Deposit\n' + 
            '2. Withdraw\n' + 
            '3. Transfer\n' + 
            '4. Transaction History\n' + 
            '5. Delete Account\n' + 
            '6. Log Out')

    term.print_menu(menu, 'How can I help you today?')

    choice = input('Please enter your choice: ')

    match choice:
        case '1':
            term.clear()
            trans.deposit(name, key)
            user_menu(name, key)
        case '2':
            term.clear()
            trans.withdraw(name, key)
            user_menu(name, key)
        case '3':
            term.clear()
            trans.transfer(name, key)
            user_menu(name, key)
        case '4':
            term.clear()
            trans.get_history(name, key)
            user_menu(name, key)
        case '5':
            term.clear()
            base.remove_user(name)
            main_menu()
        case '6':
            term.clear()
            term.print_header('See you next time, ' + name + '!')
            main_menu()
        case _:
            term.clear()
            term.print_error('Invalid input!')
            user_menu(name, key)

#Main method
if __name__ == '__main__':

    term.clear()
    term.print_header("Welcome to the PicoCoin terminal!")
    main_menu()