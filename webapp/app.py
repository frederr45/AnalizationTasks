import flask
from flask import Flask, render_template, request, jsonify
import traceback
import pickle

import task2
import task3


from for_json import predicts

# App definition
app = Flask(__name__, template_folder='templates')

# importing models
with open('model/model.pkl', 'rb') as file:
    classifier = pickle.load(file)

with open('model/model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)


@app.route('/')
def welcome():
    page_title = "Start Page"
    descr_task = "Для перехода по номеру задания, кликните на ссылку ниже"
    return render_template('welcome.html',
                           page_title=page_title,
                           descr_task=descr_task)


@app.route('/task_1', methods=['POST', 'GET'])
def task_1():
    if flask.request.method == 'GET':
        page_title = "TASK_1"
        descr_task = "Внедрение модели машинного обучения"
        return render_template('task1.html',
                               page_title=page_title,
                               descr_task=descr_task)

    if flask.request.method == 'POST':
        try:
            json_ = request.json
            final_list = []
            if isinstance(json_, dict):
                final_list.append(predicts(json_, model_columns, classifier))
            else:
                for js_ in json_:
                    final_list.append(predicts(js_, model_columns, classifier))

            return jsonify(*final_list)
        except Exception:
            return jsonify({
                "trace": traceback.format_exc()
                })


@app.route('/task_2')
def task_2():
    page_title = "TASK_2"
    descr_task = """Проанализировать выборку страховых событий
    (ДТП с двумя участниками) на возможное мошенничество.
    Выделить тех клиентов, относительно которых существует
    подозрение на мошеннические действия"""
    possibly_relatives = {
        i[0] + ' и ' + i[1]: i[2] for i in task2.possibly_relatives}
    filtered_female = {i[0]: i[1] for i in task2.filtered_female}
    filtered_male = {i[0]: i[1] for i in task2.filtered_male}
    return render_template('task2.html',
                           page_title=page_title,
                           descr_task=descr_task,
                           possibly_relatives=possibly_relatives,
                           filtered_female=filtered_female,
                           filtered_male=filtered_male)


@app.route('/task_3')
def task_3():
    page_title = "TASK_3"
    descr_task = """Проанализировать клиентов в выборке,
    провести кластеризацию, сделать описание сегментов"""
    dict_ = task3.dict_
    return render_template('task3.html',
                           page_title=page_title,
                           descr_task=descr_task,
                           dict_=dict_)
