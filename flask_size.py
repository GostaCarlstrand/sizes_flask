from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

def main():
    pass


if __name__ == "__main__":
    main()
