
# coding: utf-8

# #### 2.2. Textblob NLP Feature Extraction

# In[5]:


from textblob import TextBlob
import nltk
#nltk.download('brown')


# In[4]:


def get_textblob_features(sentence):
    
    blob = TextBlob(sentence)
    
    textblob_dict = {}
    
    ## Number of noun phrases in the sentence
    textblob_dict['Number of Noun Phrases'] = len(list(blob.noun_phrases))
    
    ## Number of POS tags in the sentence
    textblob_dict['Number of POS tags'] = len(list(blob.pos_tags))
    
    ## Polarity of the sentence
    textblob_dict['Sentence Polarity'] = blob.sentiment_assessments.polarity
    
    ## Polarity of the sentence
    textblob_dict['Sentence Subjectivity'] = blob.sentiment_assessments.polarity
    
    ## Number of words in the processed sentence
    textblob_dict['Number of words'] = len(list(blob.words))
    
    ## Language of the sentence
    textblob_dict['Language Detected'] = blob.detect_language()
    
    return textblob_dict

