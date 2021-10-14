from flask import Flask, request
from os.path import abspath
from base64 import b64encode, b64decode
from urllib.parse import unquote, urlparse, urljoin

app = Flask(__name__)

whitelist = ["http://127.0.0.1/static/images/",
             "http://localhost/static/images/"]
blacklist = ["admin", "flag"]
remove_list = ["'", "OR", "SELECT", "FROM", ";", "../", "./", "....//"]


def parse(data):
    parsed_data = [obj.replace("'", '').replace('"', '').split(
        ':') for obj in data.decode()[1:][:-1].split(',')]
    # return (parsed_data)
    built_data = {}
    for obj in parsed_data:
        print(obj[0], obj[1])
        if obj[0] == "img":
            obj[1] = b64decode(bytes(obj[1], 'utf-8')).decode()
        built_data[obj[0]] = obj[1]
    return built_data


@app.route("/post", methods=['POST'])
def post():
    pdata = parse(request.data)
    url = pdata.get('img')
    ###
    resp = unquote(url)
    ###
    whitelist_check = False
    for uri in whitelist:
        if resp.lower().startswith(uri):
            whitelist_check = uri
            break
    if whitelist_check == False:
        return ""
    ###
    for forbidden in blacklist:
        if forbidden in resp.lower():
            return ""
    ###
    for badstr in remove_list:
        resp = resp.replace(badstr, "BLOCKEDBY1337WAF")
    ###
    resp = urlparse(resp)
    resp = unquote(abspath(resp.path))
    return urljoin(whitelist_check, resp)


@ app.route("/")
def test():
    return """


%s
""" % open(__file__).read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
