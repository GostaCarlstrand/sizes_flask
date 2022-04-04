import json

from flask import Flask, render_template, request, flash, Response, redirect, url_for
from mongo_access import get_latest_persons, add

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
persons = get_latest_persons(10)


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/submit')
def submit_data():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    gender = (request.form['gender'])
    size = add(height, weight, gender)
    flash(size)
    return redirect(url_for('index'))


@app.get('/js_data')
def get_js_data():
    persons = get_latest_persons(50)
    persons_w_g = []
    for person in persons:
        persons_dict = {
            'size_value': person['size_value'],
            'gender': person['gender']
        }
        persons_w_g.append(persons_dict)
    return Response(json.dumps(persons_w_g), 200, content_type='application/json')


if __name__ == "__main__":
    app.run(debug=True)
