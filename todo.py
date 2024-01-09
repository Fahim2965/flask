from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print


app = Flask(__name__)

todos = ["do work", "do more work", "and then do some more work"]

conn = pymysql.connect(
    database = "fmuntasir2_todos",
    user = "fmuntasir2",
    password = "239442965",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor
)

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        #todos.append(new_todo)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")
        cursor.close()
        conn.commit()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `todos`")
    results = cursor.fetchall()
    cursor.close()

    return render_template("todo.html.jinja", my_todos = results)


@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")
    cursor.close()
    conn.commit()
    return redirect('/')