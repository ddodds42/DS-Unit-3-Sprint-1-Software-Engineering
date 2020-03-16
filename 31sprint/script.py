'''
Used this file to test all of my .py code
'''

# from acme_report import ADJECTIVES, NOUNS, generate_products
# from random import randint, sample, uniform
from acme import *

glove = BoxingGlove('haymaker')
print('price=',glove.price)
print('weight=',glove.weight)
print('burn=',glove.flammability)

# prod = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
# print(prod)

# glove = BoxingGlove('Punchy the Third')
# prod = Product('A cool toy')

# print(glove.punch())
# print(prod.explode())
# print(glove.price)
# print(glove.identifier)
# print(prod.identifier)