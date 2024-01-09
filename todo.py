from flask import Flask, render_template, request, redirect
import pymysql 
import pymysql.cursors
from pprint import pprint as print


app = Flask(__name__)

my_todo = ["Make money", 'get legacy blade']

conn = pymysql.connect(
    database="svassell2_todos",
    user="svassell2",
    password="228426979",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todos = request.form["new_todos"]
        cursor=conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ({new_todos})")
        cursor.close()
        conn.commit

    cursor=conn.cursor()

    cursor.execute("SELECT * FROM `todos`")
    results = cursor.fetchall()

    cursor.close()
    return render_template ("todo.html.jinja", new_todos = results)



@app.route('/delete_todo/<int:todo_index>', methods= ['POST'])
def todo_delete(todo_index):
   del my_todo[todo_index]
cursor = conn.cursor()

cursor.execute(f"DELETE FROM `todos` WHERE `id=todo_index`")
cursor.close
conn.commit