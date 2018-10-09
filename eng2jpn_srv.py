#!/usr/bin/env python3

import sys
import re
import urllib.parse
from bottle import route, run, template
from bottle import request, post, get
from bottle import static_file
from googletrans import Translator as Trans

## setting
HOST = "localhost"
PORT = 8080
##

trans = Trans()

@route('/static/js/<filename>')
def js(filename):
    return static_file(filename, root="static/js")

@route('/static/css/<filename>')
def css(filename):
    return static_file(filename, root="static/css")

@route('/')
def index():
    return template("index",eng_txt=None, jpn_txt=None)

@post('/')
def translate():
    _input = request.forms.get('eng_txt',None)
    _input = urllib.parse.quote(_input,encoding="utf-8")
    _input = re.sub('%0D%0A', ' ', _input)
    _input = urllib.parse.unquote_plus(_input,encoding="utf-8")
    output = trans.translate(_input,dest='ja')
    output = re.sub('。','．\n',output.text)
    return template("index", eng_txt=_input, jpn_txt=output)

if __name__=='__main__':
    run(host=HOST,port=PORT,debug=True,reloader=True)
