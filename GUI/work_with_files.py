import os
#checking is file
if not os.path.exists("files/to_do.txt"):
    with open("files/to_do.txt", "w") as file:
        pass

#change data in file
def change_to_does_in_file(to_does_local):
    with open('files/to_do.txt', 'w') as files:
        files.writelines(to_does_local)

#get data from file
def read_to_does_from_file():
    with open('files/to_do.txt', 'r') as file:
        to_do = file.readlines()
    return to_do
