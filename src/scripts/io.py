# /usr/bin/python

# Reading Keyboard Input : Use raw_input or input


input1 = raw_input("Enter your input: ")
print("Input is {}".format(input1))

input2 = input("Enter your input: ")  # it assumes the input is a valid Python Expression. E.g
#  [ x*5 for x in range(2,10,2]
#  5 * 3
print("Input is {}".format(input2))


# Opening and closing files

# Before you can read or write, you have to use open() function

