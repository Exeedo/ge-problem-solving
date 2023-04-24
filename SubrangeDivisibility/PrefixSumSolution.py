# Time Complexity: O(n) precalculation + O(1) per query -> O(n + q)
# Additional Memory: O(n)
X = input()
N = len(X)
L = [int(digit) for digit in X]
S = [0 for _ in range(N)]
for i in range(N):
    S[i] = S[i-1] + L[i]

Q = int(input())
for _ in range(Q):
    L, R = [int(x) for x in input().split()]
    s = S[R] if L == 0 else S[R] - S[L-1]
    print("YES" if s % 3 == 0 else "NO")
