from itertools import permutations
from solution import permutation2index, index2permutation


class TestPermutationSequence(object):
    def test_permutation2index(self):
        for n in range(3, 10, 1):
            sequence = [m for m in range(1, n + 1, 1)]
            for index, permutation in enumerate(permutations(sequence)):
                assert index == permutation2index(permutation)

    def test_index2permutation(self):
        for n in range(3, 10, 1):
            sequence = [m for m in range(1, n + 1, 1)]
            for index, permutation in enumerate(permutations(sequence)):
                assert permutation == index2permutation(index, n)
