from flask import Flask, render_template, render_template_string, request, abort
app = Flask(__name__)


@app.route("/")
def index():
    def filter(s):
        blacklist = ['class', 'attr', 'mro', 'base', 'request', 'session', 'add', '+a',
                     'config', 'subclasses', 'cookies', 'headers', '\'a', '[a', ']a', '"a', '{}']
        # chr(102)%2bchr(108)%2bchr(97)%2bchr(103)%2bchr(46)%2bchr(116)%2bchr(120)%2bchr(116)
        # (chr(102),chr(108),chr(97),chr(103),chr(46),chr(116),chr(120),chr(116))|join
        # ('flag','.txt')|join
        # {%%20set%20a%20=%20((app.__doc__|list()).pop(337)|string())%20%}{{url_for.__globals__.__builtins__.open(aa).read()}}
        # {% set a = ((app.__doc__|list()).pop(177)|string()) %}
        # {{url_for.__globals__.__builtins__.open().read()}}
        block = True
        print(s.lower())
        for i in blacklist:
            if i in s.lower():
                block = False
                print(i)
                # break
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
    <!--flag in /flag.txt-->
''' % (name)
    return render_template_string(template)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
