num = 0
while num <= 5:
    print(num)
    num += 1
print("outside the loop")
print(num)

# infinte loop
"""
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2  # 4
    numberOfApples += numberOfLoops  # 4 + 0
    numberOfLoops -= 1  # -1
print("Number of apples: " + str(numberOfApples))
"""

#infinite loop
"""
num = 100
while not False:
    if num < 0:
        break
print("num is: "+str(num))
"""

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print(*'Outside of loop')


number = 2
while number <= 10:
    print(number)
    number += 2
print("Goodbye")

##
print("Hello!")
number = 10
while number >= 2:
    print(number)
    number -= 2
print("end")

# Write a while loop that sums the values 1 through end, inclusive.
# e.g for end = 6, o/p: 21 i.e. 1 + 2 + 3 + 4 + 5 + 6
end = 6
result = 0
while end >= 1:
    result += end
    end -= 1
print(result)



# for loop

school = 'Massachusetts Insitute of Technology'
# school = 'OoM'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' \
            or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1
print(numVowels)
print(numCons)


num = 10
for num in range(5):
    print(num)
print(num)  # o/p - 0,1,2,3,4,4

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print("Foo!")


for i in range(11):
    if i % 2 == 0 and i != 0:
        print(i)
print("Goodbye!")


count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))

print("another way")
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
