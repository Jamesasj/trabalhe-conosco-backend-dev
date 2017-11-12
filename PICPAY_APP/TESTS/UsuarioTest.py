from MODELO import *
import unittest
class UsuriosTestCase(unittest.TestCase):

    def test_upper(self):
         self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
        
        