True
False

b = True
print( b )

b = False
print( b )

print( 5 > 6 )
print( 6 > 5 )

print( 5 == 5 )
print( not('igual' == 'diferente') )

#function not
print( not False )

print( 5 != 6 )

# operador de inversao de byte
print( True ^ False )

# convertendo True para int >>> 1
print( int(True) )

# convertendo False para int >>> 0
print( int(False) )

# considere também
x = 1 # true
if x :
	print('print') # ok

y = 0 # false
if y :
	print('ok')
else :
	print('no') # not

z = -6 # false
if z :
	print('ok') # this
else :
	print('no')

#convertendo um digito inteiro em boolean
#convertendo um digito inteiro em boolean
print( bool(1) ) # True
print( bool(0) ) # False
print( bool(6) ) # True
print( bool(-5) ) # True


def is_even_or_odd( x ) :
    if x % 2 == 0 :
        return True
    else:
       return False

print( is_even_or_odd( 5 ) )
print( is_even_or_odd( 12 ) )