from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename, 'w')

print "---------------Extra Line To See Read Mode w-----------------"
target.close()
target = open(filename)
print target.read()
target.close()
target = open(filename, 'w')
print "--------------------------End--------------------------------"
print "If you see nothing between, that means Read Mode m already truncates the file after opening it."

print "Truncating the file. Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()

print "Now try reading it"
target = open(filename)
print target.read()
print "Now close it again"
target.close()

