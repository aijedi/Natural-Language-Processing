
# coding: utf-8

# In[1]:


#!pip install afinn


# In[2]:


from afinn import Afinn
afinn = Afinn()

def afinn_score(sentence):
    return afinn.score(sentence)

