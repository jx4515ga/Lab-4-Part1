import CamelCase
from unittest import TestCase


class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', CamelCase.camel_case('Hello World'))


    def test_capitalized(self):
        self.assertEqual('helloWorld', CamelCase.camel_case('HELLO WORLD'))

    def test_lower(self):
        self.assertEqual('helloWorld', CamelCase.camel_case('hello world'))


    def test_camel_case_empty(self):
        self.assertNotEqual(' 1152', CamelCase.camel_case('helloWorld'))
    
    def test_camel_case_numbers_punctiation(self):
        self.assertNotEqual('helloWorld', CamelCase.camel_case('helloworldhelloworld??????!!@#$'))
    
    def test_camel_case_emojis(self):
        self.assertNotEqual('helloWorld', CamelCase.camel_case('U+1F44D '))

    def test_camel_case_more_than_one_space(self):
        self.assertEqual('helloWorld', CamelCase.camel_case('Hello              World'))

    def test_camel_case_start_end_space(self):
        self.assertEqual('helloWorld', CamelCase.camel_case('    Hello World         '))
    