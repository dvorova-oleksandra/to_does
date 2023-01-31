with open('files/to_do.txt', 'r') as files:
    to_does = files.readlines()

while True:
    action = input("What do you want to do(add, complete, show, edit or exit)?Write one of this action ")
    match action.strip().lower():
        case "add":
            adding = input("Enter a todo: ") + "\n"
            to_does.append(adding)
            with open('files/to_do.txt', 'w') as files:
                files.writelines(to_does)
        case "complete":
            delete_number = int(input("Enter number, which element you want to delete ")) - 1
            delete_element = to_does[delete_number].strip('\n')
            print(f'Todo {delete_element} was removed ')
            to_does.pop(delete_number)
            with open('files/to_do.txt', 'w') as files:
                files.writelines(to_does)
        case 'show':
            for index, item in enumerate(to_does):
                item = item.strip('\n')
                print(f'{index+1} - {item}')
        case "edit":
            edit_number = int(input("Enter number, which element you want to edit "))
            edit_element = to_does[edit_number-1].strip('\n')
            print(f'This todo will be change: {edit_element}')
            to_does[edit_number-1] = input("Write changed todo: ") + "\n"
            with open('files/to_do.txt', 'w') as files:
                files.writelines(to_does)
        case 'exit':
            print('Bye!')
            break
        case _:
            print('Wrong input! Please enter correct data')
