from flask import Flask
from flask import request
from flask import config
from flask import render_template_string
from flask import Flask, session
app = Flask(__name__)

app.config['SECRET_KEY'] = "fake_secret_key"

flag_here="flag{fake_flag}"
def validate_cookie():
    username = session.get('username')
    money = session.get('money')
    if username and money:
        return True
    else:
        return False

@app.route('/')
def hello_world():
    if request.args.get('name') != None:
        session['username'] = request.args.get('name')
        session['money'] = 2000
        return 'Hello '+ request.args.get('name') + " you have "+str(session['money'])
    return "hello world"
@app.route('/flag')
def flag():
    if not validate_cookie():
        return "get out of here hacker"
    else:
        money = session.get('money')
        if money > 100000000:
            return flag_here
        else:
            return "you dont have enough money ,"+str(money)


@app.errorhandler(404)
def page_not_found(e):
    template = '''
{%% block body %%}
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
    </div> 
{%% endblock %%}
''' % (request.path)
    #print(request.path)
    if len(request.path) >16:
        return render_template_string("Oops!! hắc cơ detected"),404
    return render_template_string(template), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)