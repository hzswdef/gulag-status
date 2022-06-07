#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

from flask import Flask, render_template

from objects import cfg, utils

app = Flask(__name__, template_folder='templates')


@app.template_global()
def app_name() -> str:
    return cfg.env.app_name

@app.template_global()
def domain() -> str:
    return cfg.env.domain

@app.template_global()
def target() -> str:
    return cfg.env.target

@app.route('/')
def status():
    return render_template(
        'status.html',
        status=utils.status()
    )

if __name__ == "__main__":
    app.run(debug=cfg.env.debug, port=8000)
 