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
    times_p2i.append((end-start)/n_repeats)
    print("For n={}, {} times permutation2index cost {:.6f}s".format(n, n_repeats, end - start))

for n in range(100, 2100, 100):
    indexs = [random.randint(0, factorial(n)) for _ in range(n_repeats)]
    start = time.perf_counter()
    for i in indexs:
        index2permutation(i, n)
    end = time.perf_counter()
    times_i2p.append((end-start)/10.0)
    print("For n={}, {} times index2permutation cost {:.6f}s".format(n, n_repeats, end - start))

labelsize = 20
fontsize = 20
linewidth = 2
xlabel = [n for n in range(100,2100,100)]
line = plt.plot(xlabel, times_p2i, 'r', linewidth=linewidth)
plt.tick_params(labelsize=labelsize)
plt.grid(linestyle='--', linewidth=1)
# plt.title('p2i',fontsize=fontsize)
plt.xlabel('n', fontsize=fontsize)
plt.ylabel('Time/s', fontsize=fontsize)
plt.show()
plt.plot(xlabel, times_i2p, 'r', linewidth=linewidth)
plt.tick_params(labelsize=labelsize)
plt.grid(linestyle='--', linewidth=1)
# plt.title('i2p',fontsize=fontsize)
plt.xlabel('n', fontsize=fontsize)
plt.ylabel('Time/s', fontsize=fontsize)
plt.show()
