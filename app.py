from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # host=0.0.0.0 makes it reachable from other devices on the same network
    app.run(host='0.0.0.0', port=5001, debug=True)
