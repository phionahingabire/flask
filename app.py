from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "hello, woprld!"
if __name__ == (__name__):
    app.run()