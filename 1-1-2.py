# task2
func = {'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y,
        'sqr': lambda x, y: x * x,
        'cube': lambda x, y: x * x * x,
        'sqrt': lambda x, y: x ** 0.5,
        'abs': lambda x, y: -x if x < 0 else x,
        'reciprocal': lambda x, y: 1 / x}

entered_func = ''
digit1 = ''
digit2 = ''
print("Type a name of function and then argument(s):\n", ', '.join(func))
text = input()
for symbol in text:
    if symbol != ' ':
        if symbol.isalpha():
            entered_func += symbol
        elif symbol.isdigit() or '.' or '-' or '+':
            digit2 += symbol
    else:
        if digit1 == '':
            digit1 = digit2
            digit2 = ''
if digit1 == '':
    digit1 = digit2

print(func[entered_func](float(digit1), float(digit2)))
