from flask import Flask, render_template, request, redirect
import pymysql 
import pymysql.cursors
from pprint import pprint as print


app = Flask(__name__)

my_todo = ["get money", 'get motion']

conn = pymysql.connect(
    database="world",
    user="svassell2",
    password="228426979",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todos = request.form["new_todos"]
    return render_template ("todo.html.jinja", new_todos = todos)

@app.route('/delete_todo/<int: todo_index>', methods= ['POST'])
def todo_delete(todo_index):
    del todos[todos]
    return redirect('/')