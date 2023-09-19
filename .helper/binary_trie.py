# 参考
# https://kanpurin.hatenablog.com/entry/2021/09/05/163703
# https://kanpurin.hatenablog.com/entry/2021/12/22/001854
class BinaryTrie:
    def __init__(self, max_query=2 * 10**5, bitlen=30) -> None:
        n = max_query * bitlen
        self._nodes = [-1] * (2 * n)
        self._cnt = [0] * n
        self._id = 0
        self._bitlen = bitlen

    def size(self):
        return self._cnt[0]

    def count(self, x):
        pt = 0
        for i in range(self._bitlen - 1, -1, -1):
            y = (x >> i) & 1
            if self._nodes[2 * pt + y] == -1:
                return 0
            pt = self._nodes[2 * pt + y]

        return self._cnt[pt]

    def insert(self, x):
        pt = 0
        for i in range(self._bitlen - 1, -1, -1):
            y = (x >> i) & 1
            if self._nodes[2 * pt + y] == -1:
                self._id += 1
                self._nodes[2 * pt + y] = self._id
            self._cnt[pt] += 1
            pt = self._nodes[2 * pt + y]
        self._cnt[pt] += 1

    def remove(self, x):
        if self.count(x) == 0:
            return

        pt = 0
        for i in range(self, self._bitlen - 1, -1, -1):
            y = (x >> i) & 1
            self._cnt[pt] -= 1
            pt = self._nodes[2 * pt + y]
        self._cnt[pt] -= 1

    def kth_elm(self, x):
        pt, ans = 0, 0
        for i in range(self._bitlen - 1, -1, -1):
            ans <<= 1
            if self._nodes[2 * pt] != -1 and self._cnt[self._nodes[2 * pt]] > 0:
                if self._cnt[self._nodes[2 * pt]] >= x:
                    pt = self._nodes[2 * pt]
                else:
                    x -= self._cnt[self._nodes[2 * pt]]
                    pt = self._nodes[2 * pt + 1]
                    ans += 1
            else:
                pt = self._nodes[2 * pt + 1]
                ans += 1
        return ans

    def lower_bound(self, x):
        pt, ans = 0, 1
        for i in range(self._bitlen - 1, -1, -1):
            if pt == -1:
                break
            if (x >> i) & 1 and self._nodes[2 * pt] != -1:
                ans += self._cnt[self._nodes[2 * pt]]
            pt = self._nodes[2 * pt + ((x >> i) & 1)]
        return ans
