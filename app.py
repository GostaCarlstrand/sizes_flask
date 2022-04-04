import json

from flask import Flask, render_template, request, flash
from mongo_access import get_latest_persons, add

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
persons = get_latest_persons(100)
myVar = 15

@app.get('/')
def index():
    return render_template('index.html', persons=persons, myVar=myVar)


@app.post('/submit')
def submit_data():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    gender = (request.form['gender'])
    size = add(height, weight, gender)
    flash(size)
    return render_template('index.html', persons=persons)


@app.get('/js_data')
def get_js_data():
    persons = get_latest_persons(100)
    l = []
    for person in persons:
        l.append(json.dumps(person))
    json.dumps(persons)
    print()




if __name__ == "__main__":
    app.run(debug=True)
