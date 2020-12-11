"""
COSINE SIMILARITY
"""

def cos_sim(d1,d2):
	dot_product = 0
	magnitude_d1 = 0
	magnitude_d2 = 0
	for i,j in zip(d1,d2):
		magnitude_d1 += i**2
		magnitude_d2 += j**2
		dot_product += i*j
	return dot_product / (magnitude_d1**0.5 * magnitude_d2**0.5)

"""
EXAMPLE USAGE
"""

d1 = [3,8,7,5,2,9]
d2 = [10,8,6,6,4,5]

print(cos_sim(d1,d2))
