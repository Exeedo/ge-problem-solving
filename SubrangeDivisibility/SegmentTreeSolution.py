# Time Complexity: O(n) precalculation + O(log(n)) per query -> O(n + q*log(n))
# Additional Memory: O(n)
class node:
    main_list = []
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.val = 0
        if start == end:
            self.val = self.main_list[start]
        else:
            mid = (start + end) // 2
            self.left = node(start, mid)
            self.right = node(mid+1,end)
            self.val = self.left.val + self.right.val

    def get(self, range_start, range_end):
        if self.start > range_end or self.end < range_start:
            return 0
        if self.start >= range_start and self.end <= range_end:
            return self.val
        assert self.left and self.right
        return self.left.get(range_start, range_end) + self.right.get(range_start, range_end)
            
X = input()
N = len(X)
node.main_list = [int(digit) for digit in X]
head = node(0, N-1)
Q = int(input())
for _ in range(Q):
    L, R = [int(x) for x in input().split()]
    print("YES" if head.get(L, R) % 3 == 0 else "NO")
