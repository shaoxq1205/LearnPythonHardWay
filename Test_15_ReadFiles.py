from sys import argv
script, filename = argv
txt = open(filename)  # Keyword
print "Here's your file %r:" % filename
print txt.read()  # Keyword
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
