import string
from nltk.corpus import stopwords
import pke
from generate_summary import Summary

def extracting_keywords(text):
    #list to store our keywords
    print("1.Extracting Keywords(ProperNoun) from Fulltext...")
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
    if(quantity=='0'):
        print("2(a).Generating summary with Transformers.Pls wait!!")
        generated_summary = Summary(text)
        filtered_keywords = []
        for i in keywords_from_fulltext:
            if i.lower() in generated_summary.lower():
                filtered_keywords.append(i)
        print("2(b).Selected Keywords from summary :",filtered_keywords)
        return filtered_keywords,generated_summary
    else:
        print("2.Selected Keywords from Full Text :",keywords_from_fulltext)
        return keywords_from_fulltext,text



# f = open('article.txt','r')
# text = f.read()
# f.close()
# keywords,summary= final_keywords(text)
# these keywords will be used to extract sentences from summary text then blank will
#be given at this keyword place then will use wordnet to get more similar words to give 
# options
