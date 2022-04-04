from flask import Flask, render_template, request, flash
from mongo_access import get_latest_persons, add

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
persons = get_latest_persons()

@app.get('/')
def index():
    return render_template('index.html', persons=persons)


@app.post('/submit')
def submit_data():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    gender = (request.form['gender'])
    size = add(height, weight, gender)
    flash(size)
    return render_template('index.html', persons=persons)




if __name__ == "__main__":
    app.run()
