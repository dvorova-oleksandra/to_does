import work_with_files
import PySimpleGUI

label = PySimpleGUI.Text("Enter a todo:")
input_box = PySimpleGUI.InputText(tooltip="Input to do here", key="todo")
button_add = PySimpleGUI.Button("Add")
button_exit = PySimpleGUI.Button("Exit")



window = PySimpleGUI.Window("To-do",
                            layout=[[label, input_box, button_add], [], [button_exit]],
                            font=("Arial", 13))
while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = work_with_files.read_to_does_from_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            work_with_files.change_to_does_in_file(todos)
        case PySimpleGUI.WIN_CLOSED | 'Exit':
            break
window.close()