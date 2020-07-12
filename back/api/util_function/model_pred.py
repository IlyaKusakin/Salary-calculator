# -*- coding: utf-8 -*-
"""
Module with functions for vacancies preprocessing
 and salary predictions.

Author: Kusakin Ilya
"""


import pandas as pd
import numpy as np
import pickle
np.random.seed(42)


import pymorphy2

def my_lemming(word):
    """
    Word: some word on NL
    Returns: lemmatized word
    
    Author: Kusakin Ilya
    """
    pymorph = pymorphy2.MorphAnalyzer()  
    return pymorph.parse(word)[0].normal_form

#Russian stemmer
from nltk.stem.snowball import SnowballStemmer 
stemmer = SnowballStemmer("russian") 

import gensim
import re
import nltk
nltk.download('stopwords')

#import text tokenizer
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()

#nltk.download('stopwords')
#nltk.download('wordnet')

#import russian stopwords
from nltk.corpus import stopwords
stopWords = set(stopwords.words('russian'))


#Russian embeddings from FastText model
wv_embeddings = gensim.models.KeyedVectors.load_word2vec_format(fname='model.bin', binary=True)

#DIY dict with vectorized russian words
my_embeddings = dict()
for i in wv_embeddings.vocab:
  without_ = re.sub('_\w+', '', i)
  my_embeddings[without_]=wv_embeddings[i]


def skills_important(dataframe):
  """
    Function that checks 15 most frequent skills from vacancy.
    dataframe :  dataframe with vacancy

    Returns:
    Dataframe with 1 in columns of skills if it exists in vacancy.
    Zeroes if not exist.
    
    Author: Kusakin Ilya
  """
  skills_list =['команда',
    'коммуникация',
    'продажа',
    'программа',
    'способность',
    'объем',
    'информация',
    'автоматизация',
    'ведение',
    'переписка',
    'умение',
    'интернет',
    'планирование',
    'контроль',
    'обеспечение']

  for i in skills_list:
    dataframe[i] = np.array([0]*len(dataframe['description.lemm']))

  for i in range(len(dataframe['key_skills'])):
    text = dataframe['key_skills'][i]
    text = re.sub('[\d+\xad]', '', text)
    words = [my_lemming(word) for word in tokenizer.tokenize(re.sub('[-\’,·”–●•№~✅“=#—«|"‚».?!:;()*^&%+/]', ' ' , text.lower())) if word not in stopWords]
    try:
      for word in words:
        dataframe[word][i] = 1
    except KeyError:
      pass
  return dataframe

def text_to_onevec(text, embeddings=my_embeddings):
    """
    Function for text vectorizing
    
        text: some text for vectorizing
        embeddings: embeggings from FastText model
        
        returns: averaged representation of text
        
        Author: Kusakin Ilya
        
    """
    text = re.sub('[\t\n]', ' ', text.lower())
    text = re.sub('[\d+\xad]', '', text)
    words = [word for word in tokenizer.tokenize(re.sub('[-\’,·”–●•№~✅“=#—«"‚»|.?!:;()*^&%+/]', ' ' , text)) if word not in stopWords]
    #print(words)
    n_known = 0
    result = 0
    for word in words:
      flag_known=0
      if my_lemming(word) in embeddings:
             result+=embeddings[my_lemming(word)]
             flag_known += 1
      if flag_known==0 and stemmer.stem(word) in embeddings:
           result+=embeddings[stemmer.stem(word)]
           flag_known += 1
      if flag_known>0:
         n_known+=1
                    
    if n_known == 0:
      return np.array([0]*300)
    else:
      return result/n_known
  
def descrs(dataframe):
    """
    Function for description vectorizing:
        
        dataframe: dataframe with column of descriptions
        
        returns: dataframe with features 
        of vectorized descriontion representation
        
        Author: Kusakin Ilya
    
    """
    dataframe['description.lemm'] = dataframe['description.lemm'].fillna('unknown') 
    descrs_vec = []
    for i in dataframe['description.lemm']:
        descrs_vec.append(text_to_onevec(i))
    descrs_df = pd.DataFrame(descrs_vec)
    name_descrs=[]
    for i in range(1,301):
      name_descrs.append('descrs_vec_'+str(i))
    descrs_df.columns = name_descrs

    return pd.concat([dataframe, descrs_df], axis=1)

def companys(dataframe):
  """
    Function for company title vectorizing
    
        dataframe: dataframe with column of companys titles
        
        returns: dataframe with vectorized representation of company title
        
        Author: Kusakin Ilya
  """
    
  dataframe['company'] = dataframe['company'].fillna('unknown')
  company_vec = []
  for i in dataframe['company']:
      company_vec.append(text_to_onevec(i))
  company_df = pd.DataFrame(company_vec)
  name_company=[]
  for i in range(1,301):
    name_company.append('company_vec_'+str(i))
  company_df.columns = name_company
  
  return pd.concat([dataframe, company_df], axis=1)

def titles(dataframe):
  """
    Function for vacancy title vectorizing
    
    dataframe: dataframe with column of vacancy titles
    
    returns: dataframe with vectorized representation of vacancy titles
    
    Author: Kusakin Ilya
  """
  dataframe['name.lemm'] = dataframe['name.lemm'].fillna('unknown')
  title_vec = []
  for i in dataframe['name.lemm']:
      title_vec.append(text_to_onevec(i))
  title_df = pd.DataFrame(title_vec)
  name_title=[]
  for i in range(1,301):
    name_title.append('title_vec_'+str(i))
  title_df.columns = name_title
  
  return pd.concat([dataframe, title_df], axis=1)

def model_prediction(title, company, employment, schedule, experience, skills, descr):
    """
    Function with preprocessing pipeline and XGBoost-model prediction 
    for web-application.
    
    Parameters
    ----------
    title : string
        title of vacancy
    company : string
        company title
    employment : string
        type of employment
    schedule : string
        type of schedule.
    experience : string
        Job experience.
    skills : string
        Text witn description of required skills.
    descr : string
        vacancy description.

    returns: salary prediction.

    Author: Kusakin Ilya
    """
    #dataframe template
    df = pd.read_csv("start.csv" , sep=";")
    
    #preprocessing pipeline
    df['experience.name'] = int(experience)
    df[employment] = 1
    df[schedule] = 1
    df = companys(df)
    df = titles(df)
    df = skills_important(df)
    df = descrs(df)
    df = df.drop(['company', 'description.lemm', 'name.lemm', 'key_skills'], axis=1)
    
    dataframe_np = np.array(df)
    #uploading model using pickle
    model =pickle.load(open("model_95sal_full.pickle.dat", "rb"))
    
    #predincting salary value    
    pred_value = model.predict(dataframe_np)
    return str(int(pred_value[0]))
