import random
import string

class PasswordGenerator:

    def __init__(self):
        self.caracters = string.ascii_letters + string.digits + string.punctuation  + " ñºª€ç¡¿¬µ"
        
    def new_password(self, password_len = 40):
        password = ''.join(random.choice(self.caracters) for _ in range(password_len))
        return password
