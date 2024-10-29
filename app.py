#decorator app.route(), used for URL Mapping

from flask import Flask, render_template,request,redirect,url_for

#initialize app as Flask app

app = Flask(__name__)

#CReate list of dictionaries to represent records

tasks = [
    {'id': 1, 'title': "Buy Groceries", 'description': "Milk, Bread, Flour, Sugar"},
    {'id': 2, 'title': "Study", 'description': "Review Python Flask!"},
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        # get a new id for our next record

        new_id= len(tasks)+1
        title = request.form['title']
        description = request.form['description']

      #  add new record to the list of task dictionary

        tasks.append({'id': new_id, 'title': title, 'description': description})
        return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
# to access a global variable that wont be overriden: Global : key word that maintains vlues of global scoped variable even on assignment

    global tasks
#LIST Comprehesnion: Loop interables and returns the end vallue as a list
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=["GET","POST"])
def edit(id):
    task = next((task for task in tasks if task['id'] == id), None)
    print(task)

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)


if __name__ == '__main__':
    app.run(debug=True, port=5000)