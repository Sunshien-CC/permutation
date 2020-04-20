import functools
import typing
import math

@functools.lru_cache(maxsize=128)
def factorial(i: int):
    return math.factorial(i)


def permutation2index(permutation: typing.Iterable):
    n = len(permutation)
    index = 0
    for i in range(n - 1):
        count = 0
        for j in range(i + 1, n, 1):
            if permutation[j] < permutation[i]:
                count += 1
        index += factorial(n - i - 1) * count
    return index


def index2permutation(index: int, n: int):
    flags = [False for _ in range(n)]
    permutation = []
    for i in range(n):
        k = index / factorial(n - i - 1)
        index = index % factorial(n - i - 1)
        for j in range(n):
            if flags[j] == False:
                k -= 1
            if k < 0:
                break
        flags[j] = True
        permutation.append(j + 1)

    return tuple(permutation)
