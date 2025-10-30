# fizzbuzz.py
i = 1
while i <= 100:
    answer = ''
    if i % 3 == 0:
        answer = answer + 'Fizz'
    if i % 5 == 0:
        answer = answer + 'Buzz'
    if len(answer) == 0:
        answer = i
    print(answer)
    i = i + 1
