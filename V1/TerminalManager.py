#This here is going to take care of things like clearing the screen and printing colored text
#Just adds a bit of polish and cleanliness to the overall user experience.
from rich import print
from rich.panel import Panel
from os import system, name

#Clear the terminal
def clear():
    
    if name == 'nt': #If we're on Windows
        _ = system('cls')
    else: #If we're on any other operating system Linux/MacOS
        _ = system('clear')
#Print an error to the console
def print_error(message: str):
    print('[red]' + message)

#Print a header in gold
def print_header(message: str):
    print('[yellow][bold][underline]' + message)

#Print a success in green
def print_success(message: str):
    print('[green]' + message)

#Print a public key
def print_key(message: str):
    print('[cyan]' + message)

def print_menu(message: str, title: str):
    print(Panel.fit(message, title=title))