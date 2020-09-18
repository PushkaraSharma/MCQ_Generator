import string
from nltk.corpus import stopwords
import pke
from generate_summary import Summary

def extracting_keywords(text):
    #list to store our keywords
    keywords = []
    #initialize extractor
    extractor = pke.unsupervised.MultipartiteRank()
    extractor.load_document(text)
    #we want to extract proper noun
    pos = {'PROPN'}
    
    #define stopwords and others
    stoplist = list(string.punctuation)
    stoplist+= stopwords.words('english')
    stoplist+= ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    
    extractor.candidate_selection(pos=pos,stoplist=stoplist)
    
    extractor.candidate_weighting()
    keyphrases = extractor.get_n_best(n=15)
    for i in keyphrases:
        keywords.append(i[0])
    return keywords

def final_keywords(text,quantity):
    
    keywords_from_fulltext = extracting_keywords(text)
   # print("Keywords from full text :",keywords_from_fulltext)
    if(quantity=='low'):
        generated_summary = Summary(text)
        filtered_keywords = []
        for i in keywords_from_fulltext:
            if i.lower() in generated_summary.lower():
                filtered_keywords.append(i)
        print("Keywords from summary :",filtered_keywords)
        return filtered_keywords,generated_summary
    else:
        return keywords_from_fulltext,text



# f = open('article.txt','r')
# text = f.read()
# f.close()
# keywords,summary= final_keywords(text)
# these keywords will be used to extract sentences from summary text then blank will
#be given at this keyword place then will use wordnet to get more similar words to give 
# options