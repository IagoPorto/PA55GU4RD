from password_generation.PasswordGenerator import PasswordGenerator

generator = PasswordGenerator() 
new_password = generator.new_password()
print("Password generated:", new_password)