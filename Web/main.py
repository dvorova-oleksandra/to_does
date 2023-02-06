import streamlit as interface
import work_with_files

todoes = work_with_files.read_to_does_from_file()

# add new to do in list
def add_todo():
    todo = interface.session_state['new_todo'] +"\n"
    todoes.append(todo)
    work_with_files.change_to_does_in_file(todoes)


#interface of program
interface.title("My simple Todo App")
interface.subheader("To do:")

#show list of todoes and complete
for index, todo in enumerate(todoes):
    checking = interface.checkbox(todo, key=todo)
    if checking:
        todoes.pop(index)
        work_with_files.change_to_does_in_file(todoes)
        del interface.session_state[todo]
        interface.experimental_rerun()

#field for adding new elments
interface.text_input(label="",
                     placeholder="Write new todo and press Enter",
                     on_change=add_todo, key='new_todo')

