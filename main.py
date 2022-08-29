a_n = 1500

S = 0
for n in range(1, 25 + 1):
    a_n = a_n - 100
    S += a_n
    print('n, a_n, S_n, = {}, {}, {}'.format(n, a_n, S))
