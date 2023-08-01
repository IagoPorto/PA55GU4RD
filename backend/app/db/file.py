class File:


    def __init__(self):
        pass


    def save(self, tuple, file_name):

        try:
            with open(file_name, 'a') as file:
                file.write(tuple)
                file.write("\n")
            print("Password saved correctly\n")
        except IOError:
            print("Error saving password\n")


    def read(self, service, file_name):

        try:
            with open(file_name, 'r') as file:
                for line in file:   
                    aux = line.strip().split(" ")[0]
                    if aux == service:
                        print(line)
                        break
                else:                   
                    print("{} service not found in file".format(service))
        except FileNotFoundError:
            print("The File '{}' doesn't exist.\n".format(file_name))
        except IOError:
            print("Error reading the file:", file_name)


    def read_all(self, file_name):

        try:
            with open(file_name, 'r') as file:
                content = file.read()
                print("\n\t\tPasswords: \n")
                print(content + "\n")
        except FileNotFoundError:
            print("The File '{}' doesn't exist.\n".format(file_name))
        except IOError:
            print("Error reading the file:", file_name)


    def update(self, service, new_tuple, file_name):

        try:
            with open(file_name, 'r') as file:
                lines = (line.rstrip() for line in file)
                altered_lines = [new_tuple if line.split(" ")[0] == service else line for line in lines] 
            with open(file_name, "w") as file:            
                file.write('\n'.join(altered_lines) + '\n')
        except FileNotFoundError:
            print("The File '{}' doesn't exist.\n".format(file_name))
        except IOError:
            print("Error reading the file:", file_name)


    def delete(self, service, file_name):

        try:     
            with open(file_name, 'r') as file:
                lines = file.readlines()
            lines = [line for line in lines if line.strip().split(" ")[0] != service]
            with open(file_name, 'w') as file:
                file.writelines(lines)
            print("Password successfully deleted\n")
        except FileNotFoundError:
            print("The File '{}' doesn't exist.\n".format(file_name))
        except IOError:
            print("Error reading the file:", file_name)