from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/logout")
def logout():
    return "<h1>User is Logged Out</h1>"
if __name__ =="__main__":
    app.run()