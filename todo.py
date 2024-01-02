from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = ["make bread", "make more bread"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todos = request.form["new_todos"]
        todos.append(new_todos)
    return render_template ("todo.html.jinja", new_todos = todos)

@app.route('/delete_todo/<int: todo_index>', methods= ['POST'])
def todo_delete(todo_index):
    del todos[todos]
    return redirect('/')