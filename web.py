import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    to_do = st.session_state["new_todo"] +"\n"
    todos.append(to_do)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbok = st.checkbox(todo, key=todo)
    if checkbok:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo,key="new_todo")

#print("hello")

#st.session_state


