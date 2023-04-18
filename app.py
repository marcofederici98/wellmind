from flask import Flask, render_template, request
import functions

questions = ['Lorem ipsum dolor? (1)', 'Lorem ipsum dolor? (2)']
answers = [['a', 'b', 'c'], ['a', 'b', 'c', 'd']]
global n
n = 0

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', quest = functions.quest_gen())

@app.route("/echo", methods =['POST'])
def echo():
    quest1 = ''
    quest2 = ''
    quest3 = ''
    age = ''
    quest1=request.form['quest1'].upper()
    quest2 = request.form['quest2'].upper()
    quest3 = request.form['quest3'].upper()
    age = request.form['age']
    print(quest1, quest2, quest3, age)
    return f"{quest1, quest2, quest3, age}"


if __name__ == '__main__':
    app.run(debug=True)