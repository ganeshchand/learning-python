# Exercise 9 - Advanced Printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:\n", days
print"Here are the months:\n", months


print """

This is a multi-line String. All special $%@ () are 
automatically escaped and printed as is
"""

# Escape sequence


print "I am 6'2\" tall."  # Escaping " within the String
print "I am 6\'2\" tall." # Escaping both Single Quote and Double Quote

print """I am 6'2" tall"""


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\cat"

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
