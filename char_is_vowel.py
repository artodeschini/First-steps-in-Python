def is_vowel(c) :
    if len(c) > 1 :
        return False
    elif c in 'AEIOUaeiou':
        return True
    else:
        return False

def is_consonat(c) :
    if len(c) > 1:
        return False
    elif c.isalpha() and not c in 'AEIOUaeiou':
        return True
    else:
        return False

char = input('type a character\n')
message = f'{char} is'

message += '' if is_vowel(char) else ' not '
message += ' a vowel'


print(message)

char = input('type a character\n')
message = f'{char} is'
message += '' if  is_consonat(char) else ' not '
message += ' a consonant'

print(message)