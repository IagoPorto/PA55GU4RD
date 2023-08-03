from src.password_generation.PasswordGenerator import PasswordGenerator
from src.cipher.SecretPassword import SecretPassword
from src.console_menu.menu import Menu
from src.db.file import File
from src.cipher.cipher import AES
from dotenv import load_dotenv

import os
import sys

def new_tuple():
    new_password = generator.new_password()
    service = input("\nWhat service do you want to save it for? ")
    return (service, new_password)

load_dotenv()
file_name = os.getenv("file_name")
generator = PasswordGenerator() 
file = File()
cipher = AES()
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
        service, new_password = new_tuple()
        secret_password = input("Please, introduce the secret password: ")
        iv, ciphertext, tag = cipher.encrypt_data(secret_password, new_password)
        print("New password: ")
        print(new_password)
        print("iv: ")
        print(iv)
        print("tag: ")
        print(tag)
        print("cipher: ")
        print(cipher)
        tuple = service + " -> " + iv.hex() + " ;; " + tag.hex() + " ;; " + ciphertext.hex()
        file.save(tuple, file_name)

    elif(user_choice == '2'):
        service = input("\nFor which service would you like to see the password? ")
        line = file.read(service, file_name)
        secret_password = input("Please, introduce the secret password: ")
        parts = line.strip().split(" ;; ")
        password = cipher.decrypt_data(secret_password.encode('utf-8'), bytes.fromhex(parts[0]), bytes.fromhex(parts[2]), bytes.fromhex(parts[1]))
        print("Your password: " + password)

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