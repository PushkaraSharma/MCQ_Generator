#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:58:08 2020

@author: pushkara
"""

from flask import Flask,render_template
import pandas as pd
from gen_mcq import display


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/result/',methods=['GET','POST'])
def mcq_results(text,value):    
    display(text,value)
    data = pd.read_json('response.json')
    data  = data.to_json(orient='records')
    return data


if __name__ == "__main__":
    app.run(debug=True)