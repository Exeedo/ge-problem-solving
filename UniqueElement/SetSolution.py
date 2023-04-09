# Time Complexity: O(n)
# Additional Memory: O(n)
n = int(input())
a = [int(x) for x in input().split()]
s = set()
for x in a:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print(s.pop())
