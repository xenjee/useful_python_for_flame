import os


'''
a lot of examples on these pages:
https://www.programcreek.com/python/example/1/os.path.join
http://www.bogotobogo.com/python/python_files.php
'''

print '-' * 30
#############################

# dummy paths:
mypath1 = '/some/folder/on/my/computer'
mypath2 = '/another/location/somewhere'


print 'mypath1: ' + mypath1
print 'mypath2: ' + mypath2
print ''

# OS PATH SPLIT & JOIN - 1
# First split the paths:
split_my_path1 = mypath1.split('/')
split_my_path2 = mypath2.split('/')

print 'split_my_path1[1:] > ', split_my_path1[1:]
print 'split_my_path2[1:] > ', split_my_path2[1:]
print ''

# Then join paths:
print 'join.(join*, join*): '
print os.path.join(os.path.join(*split_my_path1), os.path.join(*split_my_path2), "blah")

print '-' * 30
#############################

# Utility:
print 'expanduser: ' + os.path.expanduser('~')
print 'expanduser + more: ' + os.path.join(os.path.expanduser('~'), 'dir', 'subdir', 'test.py')

print '-' * 30
#############################


mypath3 = 'blah/titi'
mypath4 = 'toto/tutu'
print 'os.path.join mypath3 + mypath4 > ' + os.path.join('/', mypath3, mypath4)

print '-' * 30
#############################

# OS PATH SPLIT & JOIN - 2
pathname = "/Users/stef/dir/subdir/test.py"
os.path.split(pathname)

(dirname, filename) = os.path.split(pathname)
print 'pathname: ' + pathname
print 'dirname: ' + dirname
print 'filename: ' + filename
print ''

# splittext
(shortname, extension) = os.path.splitext(filename)

print 'shortname: ' + shortname
print 'extension: ' + extension

print '-' * 30
#############################

root = "/users"
todaystr = 'abcdef'
mylist = ('toto', 'tutu', 'titi')

print os.path.join(root, "stefan", "test", "sandboxes", todaystr, "new_sandbox", mylist[1])


print '-' * 30
#############################
