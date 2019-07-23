
# coding: utf-8

# In[1]:


import spacy

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")


# In[2]:


def get_entities(sentence):
    doc = nlp(sentence)
    
    entities_dict = {}
    for ent in doc.ents:
        entities_dict[ent.label_] =  ent.text
        
    return entities_dict

