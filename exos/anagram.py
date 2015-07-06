"""
Anagram 
(A word, phrase, or name formed by rearranging the letters of anothe)
Give a list of strings, return a list of anagram sets just from the original input.
Example:
    Input: ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    Output: [['cat', 'act'], ['tablet', 'battle', 'batlet'], ['wolf', 'flow']]
Note: It does not generate any new words that are not in the input.
"""


def anagram2(input):
    sorted_words = {}
    for word in input:
        key = ''.join(sorted(word))
        if key in sorted_words.keys():
            sorted_words[key].append(word)
        else:
            sorted_words[key] = [word]
    return [ v for v in sorted_words.values() if len(v) > 1 ]



array = ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']

print anagram2(array)
