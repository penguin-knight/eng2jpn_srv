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

def del_CRLF(input):
    _input = urllib.parse.quote(input,encoding="utf-8")
    _input = re.sub('%0D%0A', ' ', _input) # delete CRLF
    _input = re.sub('- ', '', _input)
    _input = urllib.parse.unquote_plus(_input,encoding="utf-8")
    return _input

@route('/static/js/<filename>')
def js(filename):
    return static_file(filename, root="static/js")

@route('/static/css/<filename>')
def css(filename):
    return static_file(filename, root="static/css")

@route('/')
def eng2jpn():
    return template("index",eng_txt=None, jpn_txt=None)

@route('/format_eng')
def format_eng():
    return template("format_eng",eng_txt=None)

@post('/')
def translate():
    #_input = request.forms.get('eng_txt',None)
    #_input = request.forms.eng_txt
    #_input = urllib.parse.quote(_input,encoding="utf-8")
    #_input = re.sub('%0D%0A', ' ', _input)
    #_input = re.sub('- ', '', _input)
    #_input = urllib.parse.unquote_plus(_input,encoding="utf-8")
    _input = del_CRLF(request.forms.eng_txt)
    output = trans.translate(_input,dest='ja')
    output = re.sub('。','．\n',output.text)
    output = re.sub('、','，',output)
    return template("index", eng_txt=_input, jpn_txt=output)

@post('/format_eng')
def format_eng():
    _input = del_CRLF(request.forms.eng_txt)
    return template("format_eng", eng_txt=_input)

if __name__=='__main__':
    run(host=HOST,port=PORT,debug=True,reloader=True)
