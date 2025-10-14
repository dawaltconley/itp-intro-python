# Solves FizzBuzz
for i in range(100):
    string = ''
    if i % 3 == 0:
        string += 'Fizz'
    if i % 5 == 0:
        string += 'Buzz'
    if string:
        print(string)
    else:
        print(i)
