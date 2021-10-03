#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from gen_mcq import display
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/result/', methods=['GET', 'POST'])
def mcq_results():    
    display(request.form['paragraph'], request.form['num'])
    data = pd.read_json('response.json')
    data = data.to_json(orient='records')
    print("Finally returning Response...")
    return data 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
