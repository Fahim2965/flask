from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = ["do work", "do more work", "and then do some more work"]

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        todos.append(new_todo)
    return render_template("todo.html.jinja", my_todos = todos)


@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    del todos[todo_index]

    return redirect('/')