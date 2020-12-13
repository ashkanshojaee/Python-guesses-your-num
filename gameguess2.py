import random
ok = input('Please choose a two-digit number in your mind and type OK: ')
if ok == 'OK' or ok == 'ok':
    a = 0
    z = 99
    x = random.randint(a, z)
    print('my guess is x = ', x)
    answer = input(
        'Is x  correct or bigger or smaller than your num? ( c = correct , b = bigger , s = smaller ): ')
    while answer != 'c':
        if answer == 'b':
            z = x - 1
            x = random.randint(a, z)
            print('my guess is x = ', x)
            answer = input(
                'Is x correct or bigger or smaller than your num? ( c = correct , b = bigger , s = smaller ): ')
        elif answer == 's':
            a = x + 1
            x = random.randint(a, z)
            print('my guess is x = ', x)
            answer = input('Is x  correct or bigger or smaller than your num? ( c = correct , b = bigger , s = smaller ): ')
        else:
            print('my guess is x = ', x)
            answer = input('Is x  correct or bigger or smaller than your num? ( c = correct , b = bigger , s = smaller ): ')
    print('I am Superman')
else:
    print('bye bye')
