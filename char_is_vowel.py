def is_vowel( c ) :
    if len(c) > 1 :
        return False
    elif c in 'AEIOUaeiou':
        return True
    else:
        return False


char = input('type a character\n')
message = f'{char} is'
if is_vowel( char ) :
    message += ' a vowel'
else:
    message += ' not a vowel'




