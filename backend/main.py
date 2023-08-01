from app.password_generation.PasswordGenerator import PasswordGenerator
from app.cipher.SecretPassword import SecretPassword
from app.console_menu.menu import Menu
from app.db.file import File
from dotenv import load_dotenv

import os
import sys

def new_tuple():
    new_password = generator.new_password()
    service = input("\nWhat service do you want to save it for? ")
    tuple = service + " \t --> \t " + new_password
    return tuple, service

load_dotenv()
file_name = os.getenv("file_name")
generator = PasswordGenerator() 
file = File()
user_choice = 0
secret_password  = SecretPassword()

if secret_password.there_is_password():  
   correct = False
   while not correct:
       correct = secret_password.login() 
       print(correct)
else:
    create_new_password = input("There is no password, Would you want to create a new one? (Y/N)")
    if(create_new_password.upper() == 'Y'):

        secret_password.new_password()
    else:
        Menu.bye()
        sys.exit(1)

while(user_choice != '7'):
    Menu.print_menu();
    user_choice = input("Select choice: ")

    if(user_choice == '1'):
        tuple, service = new_tuple()
        file.save(tuple, file_name)

    elif(user_choice == '2'):
        service = input("\nFor which service would you like to see the password? ")
        file.read(service, file_name)

    elif(user_choice == '3'):
        file.read_all(file_name);

    elif(user_choice == '4'):   
        tuple, service = new_tuple()
        file.update(service, tuple, file_name)

    elif(user_choice == '5'):
        service = input("\nWhich service do you want to remove? ")
        file.delete(service, file_name)

    elif(user_choice  == '6'):
        secret_password.change_password()

    elif(user_choice == '7'):
        Menu.bye()
    
    else:
        print("\nInvalid option\n")