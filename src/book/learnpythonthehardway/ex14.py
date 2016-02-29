# Exercise 14 - Prompting and Passing

from sys import argv

script, userName = argv

prompt = '>'

print "Hi {}, I am the {} script.".format(userName, script)
print "I'd like to ask you a few questions."

print "Do you like me {}?".format(userName)
likes = raw_input(prompt)

print "Where do you live {}".format(userName)
lives = raw_input(prompt)

print "What computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
""".format(likes, lives, computer)

