from password_generation.PasswordGenerator import PasswordGenerator
from console_menu.menu import Menu
from bd.file import File
from variable import Variable

generator = PasswordGenerator() 
file = File(Variable.file_name)
user_choice = 0

while(user_choice != '6'):

    Menu.print_menu();
    user_choice = input("Select choice: ")

    if(user_choice == '1'):

        new_password = generator.new_password()
        service = input("What service do you want to save it for? ")
        tuple = service + " \t --> \t " + new_password
        file.save(tuple)

    elif(user_choice == '2'):

        service = input("For which service would you like to see the password? ")
        file.read(service)

    elif(user_choice == '3'):

        file.read_all();

    else:

        Menu.bye()