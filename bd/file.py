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