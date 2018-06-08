# Some examples from:
#
import os
import glob


###################### other stuff ######################

print '-' * 20
##############

print 'now in: ' + os.getcwd()
# print os.path.realpath('test1.py')

print '-' * 20
##############


os.chdir('../join_examples')
# print '-' * 10

print 'now in: ' + os.getcwd()

print '-' * 20
##############


###################### NOW GLOB ######################

print 'From where we are now, files found using the glob.glob() method:'
for file in glob.glob("*.py"):
    print '-' + file

print '-' * 20
##############
