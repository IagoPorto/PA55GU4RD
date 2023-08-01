import os
import os.path
import bcrypt
from dotenv import load_dotenv

class SecretPassword:

    def __init__(self):
        load_dotenv()
        self.secret_file = os.getenv("file_secret")

    def thereIsPassword(self):
        try:
            if os.path.getsize(self.secret_file) == 0 :
                return False
            else:
                return True
        except FileNotFoundError:
            return False
        
    def savePassword(self, password):
        try:
            with open(self.secret_file, 'a') as file:
                file.write(password + "\n")
            print("Password saved correctly\n")
        except IOError:
            print("Error saving password\n")

    def newPassword(self):
        newPassword = input("\nPlaese, enter the new secret password: ")
        self.savePassword(str(self.hash_password(newPassword)))

    def hash_password(slef, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def check_password(self, password, password_to_check):
        return bcrypt.checkpw(password_to_check.encode('utf-8'), password.encode('utf-8'))


    def login(self):
        password = input("\nPlease, enter the password: ")
        try:
            with open(self.secret_file, 'r') as file:
                for line in file: 
                    aux = line.strip()
                    break
                else:
                    print("There is no password saved\n")
                return self.check_password(aux, password)
        except FileNotFoundError:
            print("The File '{}' doesn't exist.\n".format(self.secret_file))
            return False
        except IOError:
            print("Error reading the file:", self.secret_filet)
            return False
        
    def changePassword(self):
        password = input("\nPlease, enter the new password: ")
        hash_password = str(self.hash_password(password))
        try:
            with open(self.secret_file, 'w') as file:
                file.write(hash_password + "\n")
            print("Password saved correctly\n")
        except IOError:
            print("Error saving password\n")
             