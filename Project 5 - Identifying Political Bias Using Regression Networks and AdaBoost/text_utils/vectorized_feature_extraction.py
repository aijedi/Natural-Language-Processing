
# coding: utf-8

# In[1]:


from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument, Word2VecKeyedVectors
from gensim.models import Word2Vec
from gensim.models.word2vec import Word2VecKeyedVectors
word2vecModel = Word2VecKeyedVectors.load_word2vec_format('models/GoogleNews-vectors-negative300.bin',binary=True)

def word_to_vec_generation(sent):
    word_to_vec_value = 0
    for word in sent.split(' '):
        try:
            word_to_vec_value += word2vecModel.word_vec(word)
        except:
            pass
        
    return word_to_vec_value


# You can also download Google’s pre-trained KeyedVectors instance from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
