"""
COSINE SIMILARITY
"""

import numpy

def cos_sim(d1,d2):
	dot_product = 0
	magnitude_d1 = 0
	magnitude_d2 = 0
	dot_product = numpy.dot(d1,d2)
	for i in d1:
		magnitude_d1 = magnitude_d1 + i**2
	for j in d2:
		magnitude_d2 = magnitude_d2 + j**2
	magnitude_d1 = magnitude_d1**0.5
	magnitude_d2 = magnitude_d2**0.5
	print(magnitude_d1, magnitude_d2)
	return dot_product / magnitude_d1 + magnitude_d2

"""
EXAMPLE USAGE
"""

d1 = [3,2,0,5,0,0,0,2,0,0]
d2 = [1,0,0,0,0,0,0,1,0,2]

print(cos_sim(d1,d2))
