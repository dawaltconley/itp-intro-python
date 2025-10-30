# lists.py

# start with these numbers (you can change the values if you like)
numbers = [4, 2, 9, 1, 3]

# loop over the list, printing each item
# replace the elipses in this file with your own code

i = 0
while i < len(numbers):
    n = numbers[i]
    print(n)
    i = i + 1

# what is their sum? add them together by looping over the list
# then print the sum

sum = 0

for n in numbers:
    sum = sum + n

print(sum)

# loop over the list to find the largest number
# then print that number

max = 0

for n in numbers:
    if n > max:
        max = n

print(max)

# now loop over the list to find the smallest number
# and print that number

min = 0

for n in numbers:
    if n < min:
        min = n

print(min)

# loop over this list of numbers and add them to a new array (unique)
# so that only unique contains only the
# this is quite a bit harder

duplicates = [4, 2, 9, 2, 3, 3, 4, 6, 8, 6, 6, 0, 10, 1, 4]
unique = []

for n in duplicates:
    is_unique = True
    for u in unique:
        if n == u:
            is_unique = False
    if is_unique:
        unique.append(n)

print(unique)
