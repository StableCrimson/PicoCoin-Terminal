import Transaction as tran
import Chain, Users

#Welcome screen
def menu():
    
    print("1: New Transaction")
    print("2: Transaction History")
    print("3: View Balance")
    print("4: New User")
    print("5: Remove User")
    print("6: Exit")

    choice = input("Enter your choice here: ")

    if choice == "1":
        tran.startTransaction()
        menu()
    elif choice == "2":
        Chain.printHistory()
        menu()
    elif choice == "3":
        Users.getBalance()
        menu()
    elif choice == "4":
        Users.newUser()
        menu()
    elif choice == "5":
        Users.removeUser()
        menu()
    elif choice == "6":
        print("Thank you for choosing PicoCoin, have a great day!")
        return 0
    else:
        print("Invalid selection! Please try again.")
        menu()

#Main method
if __name__ == "__main__":
    print("Welcome to the world's first PicoCoin terminal! How can I help you?")
    menu()