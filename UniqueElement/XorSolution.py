# Time Complexity: O(n)
# Additional Memory: O(1)
n = int(input())
xor = 0
for x in input().split():
    xor ^= int(x)
print(xor)
