from solution import permutation2index, index2permutation, factorial
import random
test_N=[5,7]
for N in test_N:
    random_index=random.randint(0, factorial(N))
    permutation=index2permutation(random_index, N)
    index=permutation2index(permutation)
    print('n=',N,'index=',random_index,'permutation=',permutation)
    print('n=',N,'permutation=',permutation,'index=',index)