
# coding: utf-8

# ### 1. Text Preprocessing
# #### 1.1. Remove Stop Words and Punctuation

# In[1]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 


# In[2]:


stop_words = set(stopwords.words('english')) 


# In[3]:


def convert_list_to_string(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x +' ' 
  
    # return string  
    return new.lower() # converting string to lowercase


# In[4]:


def remove_tags(sent):
    
    sentence_list =sent.split(' ')
    for word in sentence_list:
        if ('@' in word):
            sentence_list.remove(word)
    return convert_list_to_string(sentence_list)


# In[5]:


def remove_stopwords(sentence):

    word_tokens = word_tokenize(sentence) 

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 

    filtered_sentence = [] 

    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
            
    return convert_list_to_string(filtered_sentence)


# In[6]:


from nltk.tokenize import RegexpTokenizer

def remove_tokens(sentence):

    tokenizer = RegexpTokenizer(r'\w+')
    return convert_list_to_string(tokenizer.tokenize(sentence))


# In[7]:


import pandas as pd

#extract lemma
def extract_lemma(sent):
    parsed_text = {'word':[], 'lemma':[]}
    #for sent in doc.sentences:
    for wrd in sent:
        #extract text and lemma
        parsed_text['word'].append(wrd.text)
        parsed_text['lemma'].append(wrd.lemma)
    #return a dataframe
    return pd.DataFrame(parsed_text)


# In[8]:


from nltk.stem import WordNetLemmatizer 
  
def extract_lemma(sent):
    lemmatizer = WordNetLemmatizer() 
    word_tokens = word_tokenize(sent) 
    
    lemmatized_sentence = []
    for word in word_tokens:
        lemmatized_sentence.append(lemmatizer.lemmatize(word))
    
    return convert_list_to_string(lemmatized_sentence)


# #### 1.2. Driver Function to Process text

# In[9]:


def process_text(sentence):
    return extract_lemma(remove_tokens(remove_stopwords(remove_tags(sentence))))

