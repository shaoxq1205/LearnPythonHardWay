from sys import argv
script, fromfile, tofile = argv
src = open(fromfile, "r+")
dst = open(tofile, "w+")
dst.write(src.read())
print "-------"
print dst.read(10)  # need to close and open again to read, maybe open mode is the reason
src.close()
dst.close()
