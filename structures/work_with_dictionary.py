text = 'This is a awesome occasion. This has never happened before'

char_dictionary = {}

for char in text:
    char_dictionary[char] = char_dictionary.get(char, 0) + 1

print(char_dictionary.items())

word_dictionary = {}

for word in text.split():
    word_dictionary[word] = word_dictionary.get(word,0) + 1

print(word_dictionary.items())


