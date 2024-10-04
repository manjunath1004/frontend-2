from flask import Flask, render_template  # Ensure this import works

app = Flask(__name__)

# app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)