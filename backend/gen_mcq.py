#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:01:28 2020

@author: pushkara
"""

import requests
import json
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk,simple_lesk,cosine_lesk
from nltk.corpus import wordnet 
from find_sentances import extract_sentences
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def wordnet_distractors(syon,word):
    distractors = []
    word = word.lower()
    ori_word = word
    
    #checking if word is more than one word then make it one word with _
    if len(word.split())>0:
        word = word.replace(" ","_")
        
    hypersyon = syon.hypernyms()
    if(len(hypersyon)==0):
        return distractors
    for i in hypersyon[0].hyponyms():
        name = i.lemmas()[0].name()
        
        if(name==ori_word):
            continue
        name = name.replace("_"," ")
        name = " ".join(i.capitalize() for i in name.split())
        if name is not None and name not in distractors:
            distractors.append(name)
    return distractors


def word_sense(sentence,keyword):
    word = keyword.lower()
    #print(keyword)
    if len(word.split())>0:
        word = word.replace(" ","_")
    
    syon_sets = wordnet.synsets(word,'n')
    print(keyword)
    print(syon_sets)
    if syon_sets:
        try:
            wup = max_similarity(sentence, word, 'wup', pos='n')
            adapted_lesk_output =  adapted_lesk(sentence, word, pos='n')
            lowest_index = min(syon_sets.index(wup),syon_sets.index(adapted_lesk_output))
            return syon_sets[lowest_index]

        except:
            return syon_sets[0]
           
    else:
        return None

with open('article3.txt','r') as f:
    text = f.read()
      
filtered_sentences = extract_sentences(text)

options_for_mcq = {}
for keyword in filtered_sentences:
    print(keyword)
    wordsense = word_sense(filtered_sentences[keyword][0],keyword)
    if wordsense:
        distractors = wordnet_distractors(wordsense, keyword)
        if len(distractors)>0:
            options_for_mcq[keyword]=distractors

print(options_for_mcq)                 