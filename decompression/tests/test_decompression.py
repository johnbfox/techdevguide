import unittest
from decompression import decompress

class DecompressionTests(unittest.TestCase):
    def test_single_decompression(self):
        self.assertEqual(decompress('2[ab]'), 'abab')
    
    def test_double_decompression(self):
        self.assertEqual(decompress('3[a]4[b]'), 'aaabbbb')

    def test_two_tier_decompression(self):
        self.assertEqual(decompress('3[4[a]]2[b]'), 'aaaaaaaaaaaabb')
    
    def test_decompression_with_zero(self):
        self.assertEqual(decompress('3[ab]0[f]'), 'ababab')

