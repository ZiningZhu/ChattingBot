from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Second web app on this machine!"

@app.route("/basicRequest")
def basicRequest():
    return "The programmer hasn't given me a brain yet."
    
if __name__ == "__main__":
    app.run()
