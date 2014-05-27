import re
k = "some_tandom=1.223123, paniw=30.000, gam = 0.0003, 40 1.23  =400"


def find_bounds(idx, k):
    ''' witness extreme lazyness '''

    pattern = '(=| |,|[a-zA-Z_])'
    less = re.sub(pattern, ' ', k)
    left = less[:idx].lstrip().split(' ')[-1]
    right = less[idx:].rstrip().split(' ')[0]
    summed = left + right
    print(summed)

for idx, ch in enumerate(k):
    print(ch, '->>', end='')
    find_bounds(idx, k)