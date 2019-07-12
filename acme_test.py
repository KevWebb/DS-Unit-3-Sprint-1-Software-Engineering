import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_vals(self):
        prod = Product()
        self.assertEqual(prod.name, None)
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        prod1 = Product(price=1, weight=3) # Not so stealable...
        self.assertEqual(prod1.stealability(), 'Not so stealable...')

        prod2 = Product(price=3, weight=4) # Kinda stealable.
        self.assertEqual(prod2.stealability(), 'Kinda stealable.')

        prod3 = Product(price=3, weight=1) # Very stealable!
        self.assertEqual(prod3.stealability(), 'Very stealable!')

    def test_explode(self):
        prod1 = Product(flammability=1, weight=3) # ...fizzle.
        self.assertEqual(prod1.explode(), '...fizzle.')

        prod2 = Product(flammability=1, weight=13) # ...boom!
        self.assertEqual(prod2.explode(), '...boom!')

        prod3 = Product(flammability=1, weight=70) # ...BABOOM!!
        self.assertEqual(prod3.explode(), '...BABOOM!!')

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products(5)
        for product in products:
            self.assertEqual(len(product.name.split(' ')), 2)
            adj, noun = product.name.split(' ')
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
