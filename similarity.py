# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import unicodedata

outputFile = open('output-similarity.txt','w')

# converte csv para lista
def buldingDB(db):

    database = list()
    dbFile   = open(db,'r').readlines()
    [database.append(i.rstrip().split(',')) for i in dbFile]
    return database

# gera arquivo de saída
def output(similarity,tag1,tag2,usuario,tp_tag):

	string  = 'Usuário: ' + usuario +'\t'+ 'Foto: ' + tp_tag + '\n'
	string += 'Não recomendado: ' + tag2 + '\n'
	string += 'Recomendado: ' + tag1 + '\n'
	string += 'Similaridade: ' + str(similarity[0][0]) + '\n\n'

	outputFile.write(string)

	return True

# remove acento de todos as tags
def removeAccents(tag):
    return unicodedata.normalize('NFD', unicode(tag, 'utf-8')).encode('ascii','ignore')

# Analisa a similaridade entre as fotos, desconsiderando o usuário
def byPhoto():

    return None

# Analisa por usuário a similaridade entre tags utilizadas
def byUser():

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

# cálcula a similaridade entre duas tags
def cosine(tagSet):

	count_vectorizer = CountVectorizer()
	count_matrix = count_vectorizer.fit_transform(tagSet)
	return cosine_similarity(count_matrix[0], count_matrix[1])

if __name__ == '__main__':

    recommendedDB    = buldingDB('files/recommended.csv')
    notRecommendedDB = buldingDB('files/not-recommended.csv')
    byUser()
    #byPhoto()
    outputFile.close()