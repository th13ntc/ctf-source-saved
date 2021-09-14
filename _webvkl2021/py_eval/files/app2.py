from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/calc', methods=["GET"])
def calc():
    if not request.args.get("num1"):
        return "something miss"
    elif not request.args.get("num2"):
        return "something miss"
    elif not request.args.get("calculation"):
        return "wtf you re doing?"
    else:
        resuls = 0
        b = []
        blacklists = ["func", "code", "getattribute", "~", "system", "os", "eval",
                      "base64", "+", "popen", "commands", "subprocess", "pty", "\\", "chr", "exec",
                      "sys", "init", "class", "base", "subclasses", "builtins", "base64", "modules"]

        cal = request.args.get(
            "num1")+request.args.get("calculation")+request.args.get("num2")
        print(cal)
        for i in cal:
            if ord(i) < 32 or ord(i) > 128:
                return "wtf!"
        for i in b:
            if i in cal.lower():
                return "ahuhu"
        resuls = eval(cal)
        print(resuls)
        return str(resuls)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234)
