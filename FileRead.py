from pathlib import Path

file = str(Path.home()) + "/python.txt"

try :

    with open(file) as f:
        # the method read 'read de file' and splitlines separe by '\n'
        content = f.read().splitlines()
    print( content )
except :
    print('One error')



