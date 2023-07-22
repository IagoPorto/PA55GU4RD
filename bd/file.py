class File:


    def __init__(self, file_name):
        self.file_name = file_name


    def save(self, tuple):

        try:

            with open(self.file_name, 'a') as file:

                file.write(tuple + "\n")

            print("Password saved correctly\n")

        except IOError:

            print("Error saving password\n")


    def read_all(self):
        try:

            with open(self.file_name, 'r') as file:

                content = file.read()
                print("\n\t\tPasswords: \n")
                print(content + "\n")

        except FileNotFoundError:

            print("The File '{}' doesn't exist.\n".format(self.file_name))

        except IOError:

            print("Error reading the file:", self.file_name)


    def update(self):
        pass


    def delete(self):
        pass