import work_with_files
import PySimpleGUI

label = PySimpleGUI.Text("Enter a todo:")
input_box = PySimpleGUI.InputText(tooltip="Input to do here", key="todo")
button_add = PySimpleGUI.Button("Add")
button_exit = PySimpleGUI.Button("Exit")
list_box = PySimpleGUI.Listbox(values=work_with_files.read_to_does_from_file(), key='todos',
                               enable_events=True, size=[55,10])
button_edit = PySimpleGUI.Button("Edit")
button_complete = PySimpleGUI.Button("Complete")


window = PySimpleGUI.Window("To-do",
                            layout=[[label, input_box, button_add], [list_box, button_edit, button_complete], [button_exit]],
                            font=("Arial", 13))
while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = work_with_files.read_to_does_from_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            work_with_files.change_to_does_in_file(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo = values['todos'][0]
            new_todo = values['todo']

            todos = work_with_files.read_to_does_from_file()
            index = todos.index(todo)
            todos[index] = new_todo+"\n"
            work_with_files.change_to_does_in_file(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo = values['todos'][0]
            todos = work_with_files.read_to_does_from_file()
            index = todos.index(todo)
            todos.pop(index)
            work_with_files.change_to_does_in_file(todos)
            window["todos"].update(values=todos)
        case PySimpleGUI.WIN_CLOSED | 'Exit':
            break
window.close()