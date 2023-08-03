import os
import os.path
import bcrypt
from dotenv import load_dotenv

class SecretPassword:

    def __init__(self):
        load_dotenv()
        self.secret_file = os.getenv("file_secret")
        print(self.secret_file)

    def there_is_password(self):
        try:
            if os.path.getsize(self.secret_file) == 0 :
                return False
            else:
                return True
        except FileNotFoundError:
            return False
        
    def save_password(self, password):
        try:
            with open(self.secret_file, 'a') as file:
                file.write(password + "\n")
            print("Password saved correctly\n")
        except IOError:
            print("Error saving password\n")

    def new_password(self):
        new_user = input("\nPlease, enter the new user: ")
        new_password = input("Plaese, enter the new secret password: ")
        self.save_password(str(self.hash_password(new_user)) + " --> separator --> " + str(self.hash_password(new_password)))

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def check_password(self, password, password_to_check):
        return bcrypt.checkpw(password_to_check.encode('utf-8'), password.encode('utf-8'))


    def login(self):
        user = input("\nPease, enter the user: ")
        password = input("Please, enter the password: ")
        try:
            with open(self.secret_file, 'r') as file:
                for line in file: 
                    parts = line.strip().split(" --> separator --> ")
                    break
                else:
                    print("There is no password saved\n")

                return (self.check_password(parts[1], password) and self.check_password(parts[0], user))
        except FileNotFoundError:
            print("The File '{}' doesn't exist.\n".format(self.secret_file))
            return False
        except IOError:
            print("Error reading the file:", self.secret_filet)
            return False
        
    def change_password(self):
        user = input("\nPlease, enter the new user: ")
        password = input("Please, enter the new password: ")
        line = str(self.hash_password(new_user)) + " --> separator --> " + str(self.hash_password(new_password))
        try:
            with open(self.secret_file, 'w') as file:
                file.write(line + "\n")
            print("Password saved correctly\n")
        except IOError:
            print("Error saving password\n")
             