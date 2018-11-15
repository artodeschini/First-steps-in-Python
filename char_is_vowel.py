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
if is_vowel(char) :
    message += ' a vowel'
else:
    message += ' not a vowel'


print(message)

char = input('type a character\n')
message = f'{char} is'
if is_consonat(char) :
    message += ' a consonant'
else:
    message += ' not a consonant'

print(message)