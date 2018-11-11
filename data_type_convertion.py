# to convert anything in str use the method srt

b = True  # bool
print( type(b) )
s = str( b )  # convert in str
print( type(s) )
print( s )

# to convert str to boolean use the method bool
b = bool('True')
print( b )

b = bool('true')
print( b )

b = bool('tru')
print( b )
print( type(b) )

b = bool('false')  # look this is True
print( b )
print( type(b) )

b = bool('False')  # look this is True again
print( b )
print( type(b) )

b = bool('')  # this is real false
print( b )
print( type(b) )

b = bool( 0 )  # this is real false
print( b )
print( type(b) )

b = bool( 1 )  # this is True
print( b )
print( type(b) )

# convert int to str
s = str(1234)
print( s )
print( type(s) )

# convert str to int
i = int( s )
print( i )
print( type(i) )

# error occur
# i = int('12.1')

# convert float to str
s = str(12.34)
print( s )
print( type(s) )

# convert str to float
i = float( s )
print( i )
print( type(i) )

# convert char to int note this is, after of 'g'
i = int('a', 16)
print( i )
print( type(i) )

i = int('b', 16)
print( i )
print( type(i) )

i = int('c', 16)
print( i )
print( type(i) )

# one error ocurr i = int('g', 16)

