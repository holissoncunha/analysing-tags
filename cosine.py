# version using sklearn package
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math


def cosine(tagSet):

	count_vectorizer = CountVectorizer()
	count_matrix = count_vectorizer.fit_transform(tagSet)

	return cosine_similarity(count_matrix[0], count_matrix[1])

tag1 = "cat kitten cute playing ball white blueeyes".lower()
tag2 = "White Blueeyes Funny pet Cute Ball Playing kitten kitty Cat".lower()
tags = (tag1,tag2) # tupla
print cosine(tags)[0][0]
