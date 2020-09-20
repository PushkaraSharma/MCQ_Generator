#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from flask import Flask, render_template, request
"""
Created on Sat Sep 19 15:58:08 2020

@author: pushkara
"""

response = r'''[
    {
        "question": "Allyson had said, \"I think we'll be heading on the same trajectory for a while building bigger and better variants of  ______  that are stronger in the ways that  ______  is strong and probably with the same fundamental limitations.\"",
        "options": [
            "Bert",
            "big bird",
            "elmo"
        ],
        "extras": [],
        "answer": "Bert"
    },
    {
        "question": "All of these have traditionally been solved by individual models fit to solve one specific language task and so it looks a little bit like your kitchen: Think of the individual  ______  models like utensils that you have in your kitchen, they all have one very specific task that they do very well.",
        "options": [
            "Nlp",
            "Cybernetics",
            "Natural Language Processing"
        ],
        "extras": [],
        "answer": "Nlp"
    },
    {
        "question": "Join our own machine learning and  ______  expert Britney Muller as she breaks down exactly what BERT is and what it means for the search industry.Hey, Moz fans.",
        "options": [
            "Cybernetics",
            "Natural language processing",
            "Natural Language Processing"
        ],
        "extras": [],
        "answer": "Natural language processing"
    },
    {
        "question": "Google's growing capacity for Natural Question  ______ One thing I just have to mention because I honestly cannot get this out of my head is this Keynote by Jeff Dean of Google.",
        "options": [
            "Cognizance",
            "Incognizance",
            "Awareness",
            "Understanding"
        ],
        "extras": [
            "Know",
            "Prevision"
        ],
        "answer": "Understanding"
    },
    {
        "question": "Google's growing capacity for Natural Question UnderstandingOne thing I just have to mention because I honestly cannot get this out of my head is this  ______  by Jeff Dean of Google.",
        "options": [
            "Bone Of Contention",
            "Keynote",
            "Precedent",
            "Question"
        ],
        "extras": [],
        "answer": "Keynote"
    },
    {
        "question": "She is a professor at the  ______  of Chicago and one of the kindest people.",
        "options": [
            "University",
            "Church",
            "Administration",
            "Christendom"
        ],
        "extras": [
            "College",
            "Colony",
            "Constituency",
            "Corps"
        ],
        "answer": "University"
    },
    {
        "question": "She is a professor at the University of  ______  and one of the kindest people.",
        "options": [
            "Peoria",
            "Chicago",
            "Carbondale",
            "Champaign"
        ],
        "extras": [
            "Rockford",
            "Urbana",
            "Moline",
            "Little Wabash"
        ],
        "answer": "Chicago"
    }
]'''

# import pandas as pd
# from gen_mcq import display

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/result/', methods=['GET', 'POST'])
def mcq_results():
    # Use these signatures to pass in function
    print(request.form['paragraph'], request.form['num'])
    # display(text, value)
    # data = pd.read_json('response.json')
    # data = data.to_json(orient='records')
    time.sleep(6)
    return response  # pass JSON as string, will be parsed in JQuery


if __name__ == "__main__":
    app.run(debug=True)
