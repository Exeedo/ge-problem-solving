# Time Complexity: O(n)
# Additional Memory: O(n)
n = int(input())
a = [int(x) for x in input().split()]
freq = {}
for x in a:
    if x not in freq:
        freq[x] = 0
    freq[x] += 1
for key, val in freq.items():
    if val == 1:
        print(key)
