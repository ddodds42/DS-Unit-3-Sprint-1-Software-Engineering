'''
To better organize the vast quantities and variety of goods Acme Co. manages
and sells.
'''

from random import randint as rdm


class Product:
    '''
    The Acme Monopoly needs a neat inventory generator for its vast array
    of products. Also it needs to no which are most stealable and most
    likely to catch fire.
    '''

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = rdm(1000000, 9999999)

    def stealability(self):
        '''
        Assesses how likely this product is to be stolen from Acme with the
        variables weight and price
        '''
        s = self.price / self.weight

        if s < 0.5:
            return 'Not So Stealable...'
        elif s < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        '''
        Assesses the damage risk if the product were to explode
        '''
        x = self.flammability * self.weight

        if x < 10:
            return '...fizzle.'
        elif x < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''
    Momma said knock you out knock you out
    '''

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(self)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = rdm(1000000, 9999999)

    def explode(self):
        '''
        It doesn't explode you idiot. But it can burn...
        '''
        return "...it's a glove."

    def punch(self):
        '''
        Calculates how large of a blood transfusion you will need after
        a swift haymaker wearing this glove on the business end. Jk it just
        approximates pain.
        '''
        w = self.weight

        if w < 5:
            return 'That tickles.'
        elif w < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
