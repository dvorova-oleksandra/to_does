import work_with_files
import PySimpleGUI
import time

#create element for GUI
PySimpleGUI.theme("DarkTeal12")
label_for_date = PySimpleGUI.Text('', key="today")
label = PySimpleGUI.Text("Enter a todo:")
input_box = PySimpleGUI.InputText(tooltip="Input to do here", key="todo")
button_add = PySimpleGUI.Button("Add")
button_exit = PySimpleGUI.Button("Exit")
list_box = PySimpleGUI.Listbox(values=work_with_files.read_to_does_from_file(), key='todos',
                               enable_events=True, size=[55,10])
button_edit = PySimpleGUI.Button("Edit")
button_complete = PySimpleGUI.Button("Complete")


window = PySimpleGUI.Window("To-do",
                            layout=[[label_for_date],[label, input_box, button_add], [list_box, button_edit, button_complete], [button_exit]],
                            font=("Arial", 13))

while True:
    event, values = window.read(timeout=10)
    #input data
    window['today'].update(value=time.strftime("%d %b %Y"))
    #action
    match event:
        #adding new element to list
        case 'Add':
            todos = work_with_files.read_to_does_from_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            work_with_files.change_to_does_in_file(todos)
            window["todos"].update(values=todos)
        #editing element from list
        case "Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo']
                todos = work_with_files.read_to_does_from_file()
                index = todos.index(todo)
                todos[index] = new_todo+"\n"
                work_with_files.change_to_does_in_file(todos)
                window["todos"].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("You didn't select item in list. Please do this")
        #delete element from list
        case "Complete":
            try:
                todo = values['todos'][0]
                todos = work_with_files.read_to_does_from_file()
                todos.pop(todos.index(todo))
                work_with_files.change_to_does_in_file(todos)
                window["todos"].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("You didn't select item in list. Please do this")
        #exit
        case PySimpleGUI.WIN_CLOSED | 'Exit':
            break
window.close()