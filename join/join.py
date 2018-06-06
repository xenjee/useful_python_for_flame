'''
From https://www.programiz.com/python-programming/methods/string/join
The syntax of join() is:
string.join(iterable)	
The join() method takes an iterable - objects capable of returning its members one at a time.
Some of the example of iterables are:
	- Native datatypes - List, Tuple, String, Dictionary and Set
	- File objects and objects you define with an __iter__() or __getitem()__ method
'''


print '-' * 30
#############################

# simplest example:
print "---".join(["a", "b", "c"])


print '-' * 30
#############################

music = ["NoMeansNo", "Jesus Lizards", "Grinderman2", "Bad Religion"]
print music
# Join a list with an empty space:
print ' '.join(music) + '.'
# Join a list with a comma:
print ', '.join(music) + '.'

print '-' * 30
#############################

s = "-"
seq = ("a", "b", "c")  # This is sequence of strings.
print s.join(seq)

print '-' * 30
#############################

# For lists
numList = ['1', '2', '3', '4']
seperator = ', '
print 'With lists: ' + seperator.join(numList)

# For tupples
numTuple = ('1', '2', '3', '4')
print 'With tupples: ' + seperator.join(numTuple)

string1 = 'abc'
string2 = '123'
print 'string1: ' + string1
print 'string2: ' + string2


""" The whole string1 is appened after each character of string2 """
print 'string1.join(string2): ' + string1.join(string2)

print '-' * 30
#############################

# How join() method works for dictionaries
test = {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test = {'one': 'mat', 'two'	: 'that'}
s = ', '
print(s.join(test))

print '-' * 30
#############################
