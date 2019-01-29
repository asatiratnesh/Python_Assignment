# Python program to print all ASCII character with their values.

ascii_list = ((chr(i), i) for i in xrange(127))
print dict(ascii_list)


