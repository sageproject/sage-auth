from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    print(request.args)
    return render_template("index.html", params=request.args)

@app.route("/j")
def j():
    return jsonify([{"thing1": 45}, {"thing2": 21}, {"thing3": 32}])


if __name__ == '__main__':
    app.run(host='0.0.0.0')