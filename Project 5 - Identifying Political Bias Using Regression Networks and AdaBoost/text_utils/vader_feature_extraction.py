
# coding: utf-8

# Setting up Vader NLP.
# #### 2.1. Vader Sentiment Feature Extraction

# In[1]:


#!pip install requests
#!pip install vaderSentiment


# In[2]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


# In[3]:


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))
    return score

