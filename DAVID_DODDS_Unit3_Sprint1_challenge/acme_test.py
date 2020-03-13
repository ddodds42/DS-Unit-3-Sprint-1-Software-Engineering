import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        """Test if our theft alert metric is viable."""
        p = 50
        w = 100

        prod = Product('Test Product', price=p, weight=w)
        self.assertEqual(prod.stealability(), 'Kinda stealable.')

    def test_explode(self):
        """Test if our explosion alert metric is viable."""
        f = 2
        w = 25

        prod = Product('Test Product', flammability=f, weight=w)
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Our CEO must be an informed Leviathan with accurate reports."""

    def test_default_num_products(self):
        """Must only roll out 30 new products."""
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    # def test_legal_names(self):
    #     '''To make sure our pruduct names are syntactically proper'''
    #     prods = generate_products()
    #     self.


if __name__ == '__main__':
    unittest.main()
