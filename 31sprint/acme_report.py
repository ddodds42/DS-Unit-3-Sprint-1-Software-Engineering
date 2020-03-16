from random import randint, sample, uniform
from acme import Product

''' 
this list of adjectives ae all of the marketing buzzwords that cause Coyotes
to make impulse purchases.
'''
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']

'''
This list of nouns is all of the cheap rebranded junk coyotes like to buy.
'''
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    This function generates a list of future products so our Acme marketers
    do not have to. We can fire them and send the stock product concepts
    straight to the Acme engineers. Until we automate them, too...
    '''
    products = []
    for i in range(num_products):
        prod = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        products.append(prod)
    return products


def inventory_report(products):
    '''
    This function generates a report detailing: 1) how many new products we
    can roll out before coyotes forget they are not new, 2) The average
    price we can gauge for them, 3) the average weight of the junk products,
    and 4) how far away we should keep the lighters and matches.
    '''
    prices = []
    weights = []
    volatilities = []

    for i in range(len(products)):
        prices.append(uniform(5, 100))
        weights.append(uniform(5, 100))
        volatilities.append(uniform(0, 2.5))

    unq = len(set(products))
    av_price = sum(prices) / len(prices)
    av_wght = sum(weights) / len(weights)
    av_flam = sum(volatilities) / len(volatilities)

    return print(
        'ACME CORPORATION OFFICIAL INVENTORY REPORT \n Unique product names: ',
        unq, '\n Average price: ', av_price, '\n Average weight: ', av_wght,
        '\n Average flammability: ', av_flam
    )


if __name__ == '__main__':
    inventory_report(generate_products())