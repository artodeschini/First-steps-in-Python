from pathlib import Path

file = str(Path.home()) + "/python.txt"

try:
    f = open(file, 'w') #open method create a file in mode 'w' write
    # content of file
    f.write(
        "Hello there," +
        " here is some text. In the same line\n" +# python will convert \n to os.lines
        "We are writing" +
        " the text to the file. Another line")

    f.close()  # close file
except :
    print('one except ocurrer')