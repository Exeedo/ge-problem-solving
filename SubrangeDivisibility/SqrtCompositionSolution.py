# Time Complexity: O(n) precalculation + O(sqrt(n)) per query -> O(n + q*sqrt(n))
# Additional Memory: O(n)

# Unfortunately, this solution does not pass the time limits of the problem in Python.
# But the C++ solution passes, you check that as it is identical to this one. 

from math import sqrt, ceil
X = input()
N = len(X)
List = [int(digit) for digit in X]

block_size = ceil(sqrt(N))
block_number = ceil(N / block_size)
blocks = [0 for _ in range(block_number)]
for i in range(N):
    blocks[i // block_size] += List[i]

Q = int(input())
for _ in range(Q):
    L, R = [int(x) for x in input().split()]
    index = L
    s = 0
    while index <= R:
        if index % block_size == 0 and (index + block_size - 1) <= R:
            s += blocks[index//block_size]
            index += block_size
        else:
            s += List[index]
            index += 1
    print("YES" if s % 3 == 0 else "NO")
