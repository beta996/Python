roman = input('roman number')
current = 0
previous = 0
final = 0
conversion = {'M': 1000, 'D':500, 'C' : 100, 'L' : 50, 'X' : 10, 'V':5, 'I' : 1}
for character in range (0, len(roman)):
    current = conversion[roman[character]]
    if current <= previous:
        final += current
        previous = current
    else:
        final = final + current - 2 * previous
        previous = current
print(final)

