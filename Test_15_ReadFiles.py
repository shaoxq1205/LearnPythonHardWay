from sys import argv
script, filename = argv
txt = open(filename)  # Keyword
print "Here's your file %r:" % filename
# txt.write("Adding new stuff")   # Not working
print txt.read()  # Keyword]
txt.close()

print "Type the filename again:"
# file_again = raw_input("> ")
file_again = filename
txt_again = open(file_again)
print txt_again.read()
txt_again.close()


