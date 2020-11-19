from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

x = {"applinks": {"apps": [],"details": [{"appID": "85C9KM32UF.de.gc-gruppe.chat","paths": ["/login"]}]}}

@app.route("/apple-app-site-association")
def needed():
    return jsonify(x)
    
if __name__ == "__main__":
    app.run(debug=True)
