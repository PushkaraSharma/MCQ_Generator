from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor 
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from extract_keywords import final_keywords



def set_sentances(text):
    sentences = [sent_tokenize(text)]
    # nested list to single list
    sentences = [i for sent in sentences for i in sent]
    
    #remove short sentences
    sentences = [sent.strip() for sent in sentences if len(sent)>20]
    #print(sentences)
    return sentences


def extract_sentences(keywords,text):
    key_processor = KeywordProcessor()
    filtered_sentences = {}
    
    #adding keywords to processor and to dict
    for i in keywords:
        filtered_sentences[i]=[]
        key_processor.add_keyword(i)
        
    #calling fn to set sentences fro summary text
    sentences = set_sentances(text)
    
    #extracting sentences with given keyowords and add to dict keys
    for sent in sentences:
        keyword_searched = key_processor.extract_keywords(sent)
        for key in keyword_searched:
            filtered_sentences[key].append(sent)
    
    #sorting with longest sentence of given keyword on top
    for i in filtered_sentences.keys():
        values = filtered_sentences[i]
        values = sorted(values,key=len,reverse=True)
        filtered_sentences[i] = values
        
    print(filtered_sentences)
    return filtered_sentences
    
    
with open('article3.txt','r') as f:
    text = f.read()
    
    
keywords,summary_text = final_keywords(text)       
extract_sentences(keywords, summary_text)