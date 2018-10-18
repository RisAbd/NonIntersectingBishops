

import copy


EMPTY = '-'
BISHOP = 'д'


def empty_field(n):
    f = []
    for i in range(n):
        f.append([EMPTY] * n)
    return f


def fields(n):
    if n == 0:
        return []
    if n == 1:
        return [[[BISHOP, ], ], ]

    vs = fields(n-1)

    out = []

    for i in range(n):
        f = empty_field(n)

        f[0][i] = BISHOP

        for f2 in vs:

            fcopy = copy.deepcopy(f)

            for k, row in enumerate(f2, 1):
                for j, e in enumerate(row):
                    if j >= i:
                        j += 1
                    fcopy[k][j] = e

            out.append(fcopy)

    return out


def print_field(f):

    # for row in f:
    #     for i in row:
    #         print(i, end=' ')
    #     print()

    print('-'*(len(f)*2+3))
    for row in f:
        print('| ', end='')
        for i in row:
            print(i, end=' ')
        print('|')
    print('-'*(len(f)*2+3))


def main():

    import sys

    try:
        n = int(sys.argv[1])
    except (IndexError, ValueError) as e:
        n = 4

    fs = fields(n)

    for i, f in enumerate(fs):
        print(i+1)
        print_field(f)
        print()




if __name__ == '__main__':
    main()

