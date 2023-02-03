import work_with_files
import PySimpleGUI

label = PySimpleGUI.Text("Enter a todo:")
input_box = PySimpleGUI.InputText(tooltip="Input to do here")
button = PySimpleGUI.Button("Add")


window = PySimpleGUI.Window("To-do", layout=[[label, input_box, button], ])
window.read()
window.close()