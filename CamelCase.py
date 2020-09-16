import re

def capitalize(word):
    return word[0:1].upper() + word[1:].lower()

def lowercase(word):
    return word.lower()


def camel_case(sentence):

    remove_multiple_spaces = re.sub(r'\s+', ' ', sentence)  
    remove_surrounding_space = remove_multiple_spaces.strip()  
    words = remove_surrounding_space.split(' ') 
    first_word = lowercase(words[0])  
    capitalized_words = [ capitalize(word) for word in words[ 1: ] ]
    camel_cased_words = [first_word] + capitalized_words
    camel_cased_sentance = ''.join(camel_cased_words)
    return camel_cased_sentance

def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)

    if __name__ == '__main__':
        main()