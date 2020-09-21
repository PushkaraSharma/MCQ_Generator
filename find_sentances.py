from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor 
from extract_keywords import final_keywords



def set_sentances(text):
    print("3.Selecting Sentences based on keywords...")
    sentences = [sent_tokenize(text)]
    # nested list to single list
    sentences = [i for sent in sentences for i in sent]
    
    #remove short sentences
    sentences = [sent.strip() for sent in sentences if len(sent)>20]
    #print(sentences)
    return sentences


def extract_sentences(text,quantity):
    keywords,text = final_keywords(text,quantity)
    key_processor = KeywordProcessor()
    filtered_sentences = {}
    
    #adding keywords to processor and to dict
    for i in keywords:
        filtered_sentences[i]=[]
        key_processor.add_keyword(i)
        
    #calling fn to set sentences from summary text
    sentences = set_sentances(text)
    print("4.Filtering sentences...")
    #extracting sentences with given keywords and add to dict keys
    for sent in sentences:
        keyword_searched = key_processor.extract_keywords(sent)
        for key in keyword_searched:
            filtered_sentences[key].append(sent)
    filtered_sentences = dict([(key,val) for key,val in filtered_sentences.items() if(val)])
    
    #sorting with longest sentence of given keyword on top
    for i in filtered_sentences.keys():
        values = filtered_sentences[i]            
        values = sorted(values,key=len,reverse=True)
        filtered_sentences[i] = values
        
    print(filtered_sentences)
    return filtered_sentences
    
    
# with open('article3.txt','r') as f:
#     text = f.read()
    
    
       
# extract_sentences(text)