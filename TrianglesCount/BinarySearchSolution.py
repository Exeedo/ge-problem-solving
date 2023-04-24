# Time Complexity: O(n * n * log(n))
# Additional Memory: O(n)

n = int(input())
L = [int(x) for x in input().split()]
L.sort()

def count(i, j):
    lo, hi = j + 1, n - 1
    ans = 0
    while lo <= hi: # Binary Search Loop!
        md = (lo + hi) // 2
        if L[md] >= L[i] + L[j]:
            hi = md - 1
        else:
            lo = md + 1
            ans = md - j
    return ans

ans = 0
for i in range(0, n):
    for j in range(i + 1, n):
        add = count(i, j)
        ans += add
print(ans)
