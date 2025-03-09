# Write a function that will find all the anagrams of a word from a list
# You will be given two inputs a word and an array with words.

def is_anagram(word, words):
    list_word = sorted(list(word))
    anagrams = []
    for x in words:
        check_the_same = ''.join(y for y in x if sorted(x) == list_word)
        if check_the_same != '':
            anagrams.append(check_the_same)
    print(anagrams)
    return anagrams
