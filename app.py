from flask import Flask, render_template
import pandas_size as ps



app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
