from flask import Flask,jsonify,g
import copy
app = Flask(__name__)


@app.before_request
def set_up_data():
    g.data = [
        {'id': 1, 'title': 'task1', 'desc': 'this is task1'},
        {'id': 2, 'title': 'task1', 'desc': 'this is task2'},
        {'id': 3, 'title': 'task1', 'desc': 'this is task3'},
        {'id': 4, 'title': 'task1', 'desc': 'this is task4'},
        {'id': 5, 'title': 'task1', 'desc': 'this is task5'}
    ]

    g.task_does_not_exist = {"msg": "task does not exist"}


@app.route('api/tasks')
def get_all_tasks():
    return jsonify(g.data)

@app.route('api/tasks/<int:task_id>')
def complete_task(task_id):
    if task_id > 0 and task_id <= len(g.data):
        tmp = copy.deepcopy(g.data[task_id])
        tmp['done'] = True
        return jsonify(tmp)
    else:
        return jsonify(g.task_does_not_exist)
