import sys
import time
import subprocess
import os
import re
from datetime import datetime
from flask import *

task_dict = {}
task_num = 0

def add_task(task_text):
    global task_num
    global task_dict
    task_num += 1
    task_dict[task_num] = task_text

def remove_task(num):
    global task_dict
    task_dict.pop(num)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('site.html', task_dict=task_dict)

@app.route("/add-task")
def add_task_disp():
    return render_template('add_task.html')

@app.route("/add-task", methods=['POST'])
def add_task_input():
    global task_dict
    if request.method == 'POST':
        input_text = request.form['text']
        add_task(input_text)
    return render_template('add_task.html', return_text=("Added: '" + input_text + "'"))

@app.route("/remove-task")
def remove_task_disp():
    return render_template('remove_task.html')

@app.route("/remove-task", methods=['POST'])
def remove_task_input():
    global task_dict
    if request.method == 'POST':
        input_num = request.form['text']
        if (int(input_num, base=10)) in task_dict:
            remove_task(int(input_num, base=10))
            end_text = ("Removed Task Number: '" + input_num + "'")
        else:
            end_text = "Task Number Does Not Exist"
    return render_template('remove_task.html', return_text=end_text)

if __name__ == "__main__":
    app.run("0.0.0.0")