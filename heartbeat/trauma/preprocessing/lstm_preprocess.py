import numpy as np
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class LSTMPreprocess():
    @classmethod
    def __load_gensim_model(cls):
        model = pickle.load(open('trauma/trauma_models/gensim_model.model', 'rb'))
        return model
    
    @classmethod
    def __normilize_text(cls, text):
        stop_words = stopwords.words('english')
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in punctuation]
        tokens = [word.lower() for word in tokens if word.lower() not in stop_words]
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        return tokens

    @classmethod
    def __get_vec(cls, word, model):
        if word in model.vocab:
            return model[word]
        return np.zeros(100)

    @classmethod
    def __tokens_to_vec(cls, tokens, model):
        vectors = np.array([model.get_vector(token) for token in tokens if model.has_index_for(token)])
        return vectors

    @classmethod
    def __get_words_sum(cls, words_vec):
        tmp = np.zeros(100)
        for vec in words_vec:
            tmp += vec
        return tmp

    def transform(self, text):
        model = self.__load_gensim_model()
        text = self.__normilize_text(text)
        text = self.__tokens_to_vec(text, model)
        text = self.__get_words_sum(text)
        return text