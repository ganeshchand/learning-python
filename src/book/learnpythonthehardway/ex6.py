# Exercise 6 - Strings and Text

# You can use either ' or "

hilarious = False

joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation % hilarious

# Notice the difference

print joke_evaluation, hilarious


x = "There are %d types of people." % 10

binary = "binary"

do_not = "don't"

y = "Those who know %s and those who %s" % (binary, do_not)

print x

print y

print "I said: %r" % x  # raw

print "I also said: '%s'" % y  # '%s' is similar to %r


print "String concatenation: {}".format("abc" + "def")


# We are %r for debugging, since it displays the "raw" data of the variable
# We use %s and other formatting chars for displaying purpose

# print "This is a "%s"" % "test" you can't do this
print "This is a '%s'" % "test"





