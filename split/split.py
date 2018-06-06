#############################
print '-' * 30

my_path = '/Users/stefan/XenDrive/__WORK/PROJECTS/PULSE/18P520_python/shots/VFX_0010/3d/camera/Chair.fbx'
print my_path
split_my_path = my_path.split('/')[1:3]
print split_my_path

print '-' * 30
#############################

str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print str.split()
print str.split(' ', 1)

print '-' * 30
#############################

text = 'this is a text line'
# splits at space
print(text.split())
# Splitting at ':'
print(text.split(':'))  # looks silly, seems useless ... who knows ...
grocery = 'Fruits, Vegies, Meat, Bread'
# splits at ','
print(grocery.split(', '))
# Splitting at ':'
print(grocery.split(':'))  # looks silly too.

print '-' * 30
#############################


grocery = 'Fruits - Vegies - Meat - Bread - Water - Salt - Pepper'
# maxsplit: 0
print(grocery.split('- ', 0))
# maxsplit: 1
print(grocery.rsplit('- ', 1))
# maxsplit: 2
print(grocery.rsplit('- ', 2))
# maxsplit: 3
print(grocery.rsplit('- ', 3))

print '-' * 30
#############################

numbers = '1 - 2 - 3 - 4 - 5 - 6 - 7'
print numbers.split('- ', 2)
print numbers.split('- ', 2)[2]
print ''
print numbers.rsplit('- ', 2)
print numbers.rsplit('- ', 2)[0]


print '-' * 30
#############################
