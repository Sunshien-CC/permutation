from solution import permutation2index, index2permutation, factorial
import random
import time
import copy
import matplotlib.pyplot as plt
n_repeats = 10
times_p2i=list([])
times_i2p=list([])
for n in range(100, 2100, 100):
    sequence = list(range(1, n, 1))
    permutations = []
    for _ in range(n_repeats):
        random.shuffle(sequence)
        permutations.append(copy.copy(sequence))
    start = time.perf_counter()
    for permutation in permutations:
        permutation2index(permutation)
    end = time.perf_counter()
    times_p2i.append((end-start))
    print("For n={}, {} times permutation2index cost {:.6f}s".format(n, n_repeats, end - start))

for n in range(100, 2100, 100):
    indexs = [random.randint(0, factorial(n)) for _ in range(n_repeats)]
    start = time.perf_counter()
    for i in indexs:
        index2permutation(i, n)
    end = time.perf_counter()
    times_i2p.append((end-start))
    print("For n={}, {} times index2permutation cost {:.6f}s".format(n, n_repeats, end - start))

plt.plot([n for n in range(100,2100,100)],times_p2i)
plt.tick_params(labelsize=20)
plt.title('p2i',fontsize=20)
plt.xlabel('N',fontsize=20)
plt.ylabel('time/s',fontsize=20)
plt.show()
plt.plot([n for n in range(100,2100,100)],times_i2p)
plt.tick_params(labelsize=20)
plt.title('i2p',fontsize=20)
plt.xlabel('N',fontsize=20)
plt.ylabel('time/s',fontsize=20)
plt.show()
