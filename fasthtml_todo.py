from fasthtml.common import *

def render(todo):
    tid = f'todo-{todo.id}'
    toggle = A(
        'Toggle', hx_get=f'/toggle/{todo.id}',
         target_id=tid)
    delete = A(
        'Delete', hx_delete=f'/{todo.id}', 
        hx_swap='outerHTML', target_id=tid) # hx_swap to tell htmx what to do with None
    return Li(
        toggle, delete,
        todo.title + (' ✅' if todo.done else ''),
        id=tid)

app,rt,todos,Todo = fast_app('todos.db',live=True, render=render, id=int, title=str, done=bool, pk='id') # define database (title and doneT/F?)
# sqlite is built in
# Using a database we additionally get an object containing the table (todos)
# And an object containing the type of the thing in table

@rt('/') # define create
def get(): 
    frm = Form(Group(Input(placeholder="Add new Todo", name='title'), Button("Add")),
    hx_post='/', target_id='todo_list', hx_swap='beforeend')
    return Titled(
        "To-dos", 
        Card(
            Ul(*todos(), id='todo-list'),
            header=frm,))

@rt('/')
def post(todo:Todo):
    return todos.insert(todo) 

@rt('/{tid}') # define delete
def delete(tid:int): 
    todos.delete(tid)

@rt('/toggle/{tid}') # define what happens when we go to this path 
def get(tid:int):
    todo = todos[tid]
    todo.done = not todo.done
    return todos.update(todo)

@rt('/') # define home route
def get(): 
    return Titled("To-dos", 
    Ul(*todos()), # asterisk unpacks inidividual items in table
    )


serve()
