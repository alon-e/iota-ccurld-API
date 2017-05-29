import os
import subprocess

from app import app

myIP      = "http://localhost:3000"
net_names = []
ccurl_cmd = "./ccurld"
mwm       = " 18 "
ccurl_pipe = ".ccurld_pipe"

import string
allowed = set(string.ascii_uppercase + '9')

cmd = ccurl_cmd + mwm + ccurl_pipe + " &"
#clean up
res = os.system("killall ccurld")
try:
    os.remove(ccurl_pipe)
except OSError:
    pass
#run ccurld
res = os.system(cmd)


def check(test_str):
    if len(test_str) != 2673:
        print len(test_str)
        return False
    return (set(test_str) <= allowed)

@app.route('/')
def index():
    return "Hello"

@app.route('/curl/<string:trytes>')
def ReadMyMessages(trytes):
    #validate trytes
    if not check(trytes):
        return "-E- trytes invalid"
    with open(ccurl_pipe,"w") as fd:
        fd.write(trytes)
    with open(ccurl_pipe, "r") as fd:
        res = fd.read()

    return res