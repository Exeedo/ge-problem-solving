# Time Complexity: O(n log n)
# Additional Memory: O(1)
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
i = 0
while i+1 < len(a):
    if a[i] == a[i+1]:
        i += 2
    else:
        print(a[i])
        break
else:
    print(a[-1])
