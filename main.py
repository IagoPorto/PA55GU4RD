from password_generation.PasswordGenerator import PasswordGenerator
from console_menu.menu import Menu
from bd.file import File
from variable import Variable

generator = PasswordGenerator() 
f = File(Variable.file_name)
user_choice = 0

while(user_choice != '5'):

    Menu.print_menu();
    user_choice = input("Select choice: ")

    if(user_choice == "1"):

        new_password = generator.new_password()
        service = input("What service do you want to save it for? ")
        tuple = service + " \t --> \t " + new_password
        f.save(tuple)

    else:

        Menu.bye()