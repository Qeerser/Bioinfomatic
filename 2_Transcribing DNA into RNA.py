text = open('input.txt' , 'r').read()
text.replace("T","U")
open('output.txt' , 'w').write(text.replace("T","U"))