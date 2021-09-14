
from flask import Flask, render_template, render_template_string, request, abort
app = Flask(__name__)


@app.route("/")
def index():
    def filter(s):
        blacklist = ['class', 'builtins', 'attr', 'mro', 'base', 'request', 'session', 'add',
                     '+', 'config', 'subclasses', 'cookies', 'headers', '\'', '[', ']', '"', '{}']

        block = True
        for i in blacklist:
            if i in s.lower():
                block = False
                break
        return block
    if not request.args.get('name'):
        return open(__file__).read()
    elif filter(request.args.get('name')):
        name = request.args.get('name')
    else:
        name = 'cut dcmm'
    template = '''

    <div >
        <p>Hello, %s</p>
    </div>
    <!-- -->
''' % (name)
    return render_template_string(template)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9998)
