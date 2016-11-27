#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import flask
from flask import request

app = flask.Flask(__name__)

with app.test_request_context('/?name=Perter'):
    assert request.path == '/'
    assert request.args['name'] == 'Perter'

with app.test_client() as c:
    rv = c.get('/?tequila=42')
    assert isinstance(request.args['tequila'], str)
    assert request.args['tequila'] == '42'

# 这里将会抛出一个异常，因为是在一个请求上下文的外部调用 request 对象
# c = app.test_client()
# rv = c.get('/?answer=42')
# assert request.args['answer'] == '42'


