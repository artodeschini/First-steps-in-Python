# In python we can use simple quote or double quote to create a string

string1 = '1'
string2 = "2"

# but is a syntaxe erro
# string2 = '3"

print( type( string1 ) )

message = 'Hello World'

print( message.upper() )
# not str is imutable
print( message )
print( message.lower() )

sample = 'hello'
# this put a frist chat to upper
print( sample.capitalize() )

# islower return a boolean True if all char is lowercase False if one is upper
print( sample.islower() )
print( message.islower() )

# istitle return a boolean True if first char is upper and another lower
print( sample.capitalize().istitle() )
print( message.capitalize().istitle() )

# isupper return a boolean True if str is upper
print( sample.upper().isupper() )
print( sample.isupper() )

# isdigit return a boolean True if digit and False if is not
print( '1'.isdigit() )
print( 'A23'.isdigit() )
print( '1 2 '.isdigit() )
print( '1.2'.isdigit() )

# isalpha return a boolean True if alpha and False if is not
print( 'artur'.isalpha() )
print( '23'.isalpha() )

# isa1num return a boolena True if has one number
print( '123'.isalnum() )
print( 'Artur'.isalnum() )

# endswith return True if a str end with another in parameter
print( 'Artur Todeschini Crestani'.endswith('Crestani') )
print( 'Artur Todeschini Crestani'.endswith('Manu') )

# startswith return True if a str start with another in parameter
print( 'Artur Todeschini Crestani'.startswith('Artur') )
print( 'Artur Todeschini Crestnai'.endswith('Manu') )

# find show the position where start if not exist -1
print( 'Artur Todeschini Crestani'.find('Artur') )
print( 'Artur Todeschini Crestani'.find('Todeschini') )
print( 'Artur Todeschini Crestani'.find('Crestani') )
print( 'Artur Todeschini Crestani'.find('Manu') )