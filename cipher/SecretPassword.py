import os.path
import bcrypt
from variable import Variable

class SecretPassword:

    def __init__(self):
        pass

    def thereIsPassword(self):
        try:
            if os.path.getsize(Variable.file_secret) == 0 :
                return False
            else:
                return True
        except FileNotFoundError:
            return False
        
    def savePassword(self, password):
        try:
            with open(Variable.file_secret, 'a') as file:
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
        return bcrypt.checkpw(password.encode('utf-8'), password_to_check.encode('utf-8'))


    def login(self):
        password = input("\nPlease, enter the password: ")
        passwordHash = self.hash_password(password)
        try:
            with open(Variable.file_secret, 'r') as file:
                for line in file: 
                    aux = line.strip()
                    break
                else:
                    print("There is no password saved\n")
                self.check_password(aux, passwordHash)
        except FileNotFoundError:
            print("The File '{}' doesn't exist.\n".format(Variable.file_secret))
            return False
        except IOError:
            print("Error reading the file:", Variable.file_secret)
            return False
             