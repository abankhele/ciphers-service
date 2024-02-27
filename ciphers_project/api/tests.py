from django.test import TestCase
from .ciphers import caesar_enocde

class CiphersText(TestCase):
    def test_caeser_encoding_1(self):
        plain_text='hello'
        shift=1
        expected='ifmmp'
        output=caesar_enocde(plain_text,shift)
        self.assertEqual(expected,output)

    def test_caeser_encoding_2(self):
        plain_text='winter'
        shift=3
        expected='zlqwhu'
        output=caesar_enocde(plain_text,shift)
        self.assertEqual(expected,output)





# Create your tests here.
