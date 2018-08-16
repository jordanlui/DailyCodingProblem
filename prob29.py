# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters 
# as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. 
# You can assume the string to be encoded have no 
# digits and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.

# Run string class accepts a alpha string input and runs RunString encoder decoder
# DCP29

from RunString import RunString

# Test
list1 = 'AAAABBBCCDAA'
test = RunString(list1)
print test.input
print test.encoded
print test.decoded


list1 = 'JJJJJOORRQQQQQQQQQUIOPUIOP'
test = RunString(list1)
print test.input
print test.encoded
print test.decoded