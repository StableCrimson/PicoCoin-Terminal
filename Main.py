import Transaction as tran
import Chain

#Welcome screen
def menu():
    
    print("1: New Transaction")
    print("2: Transaction History")
    print("3: Exit")

    choice = input("Enter your choice here: ")

    if choice == "1":
        tran.startTransaction()
        menu()
    elif choice == "2":
        Chain.printHistory()
        menu()
    elif choice == "3":
        print("Thank you for choosing PicoCoin, have a great day!")
        return 0
    else:
        print("Invalid selection! Please trry again.")
        menu()

#Main method
if __name__ == "__main__":
    print("Welcome to the world's first PicoCoin terminal! How can I help you?")
    menu()