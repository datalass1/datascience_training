import lowercase_vowels
import unittest

class TestCountLowercaseVowels(unittest.TestCase):
    '''Test methods for count_lowercase_vowels'''

    def test_count_lowercase_vowels_1(self):
        '''count an empty string'''
        actual = lowercase_vowels.count_lowercase_vowels('')
        expected = 0
        self.assertEqual(expected, actual)

    def test_count_lowercase_vowels_2(self):
        '''count an single string vowel'''
        actual = lowercase_vowels.count_lowercase_vowels('a')
        expected = 1
        self.assertEqual(expected, actual)

    def test_count_lowercase_vowels_3(self):
        '''count a single string not vowel'''
        actual = lowercase_vowels.count_lowercase_vowels('x')
        expected = 0
        self.assertEqual(expected, actual)

    def test_count_lowercase_vowels_4(self):
        '''count a string of no vowels'''
        actual = lowercase_vowels.count_lowercase_vowels('xyz')
        expected = 0
        self.assertEqual(expected, actual)

    def test_count_lowercase_vowels_5(self):
        '''count a string of all vowels'''
        actual = lowercase_vowels.count_lowercase_vowels('aio')
        expected = 3
        self.assertEqual(expected, actual)

    def test_count_lowercase_vowels_6(self):
        '''count a string of mixed vowels and no vowels'''
        actual = lowercase_vowels.count_lowercase_vowels('hello')
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)


