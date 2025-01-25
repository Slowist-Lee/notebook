import re
string=input('input a string: ')
pattern=r'#+'
print(re.search(pattern,string))
# \S+\]\(\S+\)
# \]\(\S+\)

# \S+\]\(\S+\)