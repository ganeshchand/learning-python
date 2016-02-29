# Exercise 11 - Asking Questions

print "What's you name?",
name = raw_input()
print "How tall are you?",
height = raw_input()
print "How old are you?",
age = raw_input()


print "Hello, {}! You are {} years old and {} tall".format(name,age,height)

print "Hello, %r! You are %r years old and %r tall" % (name, age, height)


# raw_input() also takes parameter that you can use to prompt to a user

print "Adding Two Numbers"

x = int(raw_input("Enter the 1st Number: "))
y = int(raw_input("Enter the 2nd Number: "))
print "Sum of {} and {} is {}".format(x, y, x + y)
