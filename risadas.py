print('digite uma risada')
risada = input()

vogais = [ 'a', 'e', 'i', 'o', 'u' ]

# removendo as vogais de risada

processado = ''

for c in risada :
    if c in vogais :
        processado += c

# para fazer o reverso de uma string utilzar slice [::, -1] ou seja do inicio ao fim incremendo inverso
if processado == processado[::-1] :
    print('S')
else:
    print('N')


#w = 'word' --> word
#r = w[:: -1] --> drow

#print( list(zip(w, r)) )