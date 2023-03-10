from work_with_files import read_to_does_from_file, change_to_does_in_file
import time

#run program
while True:
    #show date
    now = time.strftime("%d %b %Y")
    print("Today: ", now)
    action = input("What do you want to do(add, complete, show, edit or exit)?Write one of this action ")
    #action
    match action.strip().lower():
        #add new to do to  list
        case "add":
            adding = input("Enter a todo: ") + "\n"
            to_does = read_to_does_from_file()
            to_does.append(adding)
            change_to_does_in_file(to_does)
        #delete element from list
        case "complete":
            try:
                delete_number = int(input("Enter number, which element you want to delete ")) - 1
                to_does = read_to_does_from_file()
                delete_element = to_does[delete_number].strip('\n')
                print(f'Todo {delete_element} was removed ')
                to_does.pop(delete_number)
                change_to_does_in_file(to_does)
            except ValueError:
                print("Invalid data. You must write number of todo")
                continue
            except IndexError:
                print("This element isn't in list")
                continue
        #show all elements from list
        case 'show':
            to_does = read_to_does_from_file()
            for index, item in enumerate(to_does):
                item = item.strip('\n')
                print(f'{index + 1} - {item}')
        #edit element in list
        case "edit":
            try:
                to_does = read_to_does_from_file()
                edit_number = int(input("Enter number, which element you want to edit "))
                edit_element = to_does[edit_number - 1].strip('\n')
                print(f'This todo will be change: {edit_element}')
                to_does[edit_number - 1] = input("Write changed todo: ") + "\n"
                change_to_does_in_file(to_does)
            except ValueError:
                print("Invalid data. You must write number of todo")
                continue
            except IndexError:
                print("This element isn't in list")
                continue
        #exit from program
        case 'exit':
            break
        case _:
            print('Wrong input! Please enter correct data')

print('Bye!')
