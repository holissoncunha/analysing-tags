# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import unicodedata

outputFile = open('output-similarity.txt','w')

def buldingDB(db):

    database = list()
    dbFile   = open(db,'r').readlines()
    [database.append(i.rstrip().split(',')) for i in dbFile]
    return database

def output(similarity,tag1,tag2,usuario,tp_tag):

    outputFile.write('Usuário: ' + usuario +'\t'+ 'Foto: ' + tp_tag + '\n')
    outputFile.write('Não recomendado: ' + tag2 + '\n')
    outputFile.write('Recomendado: ' + tag1 + '\n')
    outputFile.write('Similaridade: ' + str(similarity[0][0]) + '\n\n')
    return True

def removeAccents(tag):

    return unicodedata.normalize('NFD', unicode(tag, 'utf-8')).encode('ascii','ignore')

def similarityBuPhoto():
    
    return None


def process():

    for i in notRecommendedDB:
        tag = []
        for j in recommendedDB:
            if i[0] == j[0]:                       # verifica se é o mesmo usuário
                if i[2] == j[3]:                   # verifica se é a mesma foto
                    tag.append(j[1].lower())
        tag1 = removeAccents(' '.join(tag))
        tag2 = removeAccents(i[1].lower())
        tags = (tag1,tag2)
        similarity = cosine(tags)
        output(similarity,tag1,tag2,i[0],i[2])

    return None

def cosine(tagSet):

    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(tagSet)
    return cosine_similarity(count_matrix[0], count_matrix[1])

if __name__ == '__main__':

    recommendedDB    = buldingDB('recommended.csv')
    notRecommendedDB = buldingDB('not-recommended.csv')
    process()
    outputFile.close()