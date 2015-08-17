# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math

# not-recommended (iduser,photo1,photo2,photo3,photo4,email,gender,age)

def buldingDB(db):
    
    database = list()
    dbFile   = open(db,'r').readlines()
    [database.append(i.rstrip().split(',')) for i in dbFile]
    
    return database

def process():
    
    for index_1,i in enumerate(notRecommendedDB):
        for index_2,j in enumerate(recommendedDB):
            if i[0] == j[1]
            
    return None

def cosine(tagSet):

    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(tagSet)

    return cosine_similarity(count_matrix[0], count_matrix[1])
    
if __name__ == '__main__':
    
    recommendedDB    = buldingDB('recommended.csv')
    notRecommendedDB = buldingDB('not-recommended.csv')
    process()
    
    
    