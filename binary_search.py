print('Please think of the number from 1 to 100 and I will quess it!:\n')
total = list(range(1, 102))
print(total)
quessed = False

while not quessed:
    if len(total) < 2:
        print('Looks like I quessed, hey-hey-hey!')
        quessed = True
    half = (total[0] + total[-1]) // 2
    answer = input(f'{half}, is it M(ore), L(ess) or E(qual)?\n')
    if answer == 'M':
        total = total[total.index(half):-1]
        print(total[0])
        print(total)
    elif answer == 'L':
        total = total[0:total.index(half)]
        print(total)
    else:
        print('Hooray')
        quessed = True
