aList = [ 2,4,5,6, 3, 7,1 ]
copy = aList

print( aList )

ordenado = sorted( aList )

print( ordenado )

# pode ser utilizado também
copy.sort()
print( copy )

# ordem reverse
copy.sort( reverse= True )
print( copy )
