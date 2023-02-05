import streamlit as interface
import work_with_files

interface.title("My simple Todo App")
interface.subheader("To do:")
todoes = work_with_files.read_to_does_from_file()
for todo in todoes:
    interface.checkbox(todo)

interface.text_input(label="", placeholder="Write new todo")

