Hello #!/usr/bin/env python2

from flask import Flask
from flask import render_template, render_template_string
from flask import request
import re

app = Flask(__name__)

@app.route(&#39;/&#39;)
def index():
    return render_template(&#34;index.html&#34;)

@app.route(&#39;/submit&#39;, methods=[&#34;GET&#34;])
def submit():
    try:
        template = &#34;&#34;&#34; &lt;html&gt;
             &lt;h1&gt; Hello {}   &lt;/h1&gt;     
        &lt;/html&gt;
        &#34;&#34;&#34;.format(request.args.get(&#39;value&#39;))

    except KeyError:
        return &#34;Error, stop doing sneaky stuff here.&#34;

    filter_regex = r&#34;_|config|os|RUNCMD|base|import&#34;


    if re.search(filter_regex, template):
        return &#34;Sorry, the following keywords/characters are not allowed :- _ ,config ,os, RUNCMD, base&#34;


    return render_template_string(template)