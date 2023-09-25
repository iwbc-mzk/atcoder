import sys

sys.setrecursionlimit(10**9)


# 参考
# https://kanpurin.hatenablog.com/entry/2021/09/05/163703
# https://kanpurin.hatenablog.com/entry/2021/12/22/001854
# https://ikatakos.com/pot/programming_algorithm/data_structure/trie
class BinaryTrie:
    """
    Binary Trie
    Trie木の辺の値を文字でなく0/1に限定し、非負整数を2進数で管理する。
    """

    def __init__(self, max_query: int = 2 * 10**5, bitlen: int = 30) -> None:
        """
        初期化処理

        Args:
            max_query (int, optional): 管理する値の最大数. Defaults to 2*10**5.
            bitlen (int, optional): 管理する非負数数値を表す最大2進数桁数. Defaults to 30.
        """
        n = max_query * bitlen
        self._nodes = [-1] * (2 * n)
        self._cnt = [0] * n
        self._id = 0
        self._bitlen = bitlen

    def size(self):
        return self._cnt[0]

    def count(self, x: int) -> int:
        """
        xの個数を返す。

        Args:
            x (int): 非負整数

        Returns:
            int: xの個数
        """
        pt = 0
        for i in range(self._bitlen - 1, -1, -1):
            y = (x >> i) & 1
            if self._nodes[2 * pt + y] == -1:
                return 0
            pt = self._nodes[2 * pt + y]

        return self._cnt[pt]

    def insert(self, x: int) -> None:
        """
        非負整数xを挿入する。
        管理する値の2進数での最大桁数がdの時、計算量は O(d)

        Args:
            x (int): 非負整数
        """
        pt = 0
        for i in range(self._bitlen - 1, -1, -1):
            y = (x >> i) & 1
            if self._nodes[2 * pt + y] == -1:
                self._id += 1
                self._nodes[2 * pt + y] = self._id
            self._cnt[pt] += 1
            pt = self._nodes[2 * pt + y]
        self._cnt[pt] += 1

    def remove(self, x: int) -> None:
        """
        非負整数xを取り除く。
        xが存在しない場合は何もしない。
        管理する値の2進数での最大桁数がdの時、計算量は O(d)

        Args:
            x (int): 非負整数
        """
        if self.count(x) == 0:
            return

        pt = 0
        for i in range(self._bitlen - 1, -1, -1):
            y = (x >> i) & 1
            self._cnt[pt] -= 1
            pt = self._nodes[2 * pt + y]
        self._cnt[pt] -= 1

    def kth_elm(self, k: int) -> int:
        """
        昇順k番目の値を返す。(1-indexed)
        管理する値の2進数での最大桁数がdの時、計算量は O(d)

        Args:
            k (int): 非負整数

        Returns:
            int: k番目の値
        """
        pt, ans = 0, 0
        for _ in range(self._bitlen - 1, -1, -1):
            ans <<= 1
            if self._nodes[2 * pt] != -1 and self._cnt[self._nodes[2 * pt]] > 0:
                if self._cnt[self._nodes[2 * pt]] >= k:
                    pt = self._nodes[2 * pt]
                else:
                    k -= self._cnt[self._nodes[2 * pt]]
                    pt = self._nodes[2 * pt + 1]
                    ans += 1
            else:
                pt = self._nodes[2 * pt + 1]
                ans += 1
        return ans

    def lower_bound(self, x: int) -> int:
        """
        昇順に並べた時のx以上の最小要素の位置。(1-indexed)
        x以上の要素がない場合はsize+1
        管理する値の2進数での最大桁数がdの時、計算量は O(d)

        Args:
            x (int): 非負整数

        Returns:
            int: x以上の最小要素の位置
        """
        pt, ans = 0, 1
        for i in range(self._bitlen - 1, -1, -1):
            if pt == -1:
                break
            if (x >> i) & 1 and self._nodes[2 * pt] != -1:
                ans += self._cnt[self._nodes[2 * pt]]
            pt = self._nodes[2 * pt + ((x >> i) & 1)]
        return ans


def main():
    Q = int(input())

    N = 2**20

    bt = BinaryTrie(bitlen=60)
    [bt.insert(i) for i in range(N)]

    V = [-1 for _ in range(N)]
    for _ in range(Q):
        t, x = map(int, input().split())

        if t == 1:
            h = x % N
            i = bt.lower_bound(h)
            if i == bt.size() + 1:
                i = bt.lower_bound(0)

            v = bt.kth_elm(i)
            bt.remove(v)
            V[v] = x
        else:
            print(V[x % N])


if __name__ == "__main__":
    main()
