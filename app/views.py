#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals, division

from app import app

@app.route('/')
def index():
    return "Hello World"
