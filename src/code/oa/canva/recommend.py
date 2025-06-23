from collections import defaultdict

from httpcore import ConnectionInterface


users = [0, 1, 2, 3]
edges = [[0, 1], [1, 2], [2, 3]]
# 0 的朋友是 1；1的朋友是0和2；2的朋友是1和3；3的朋友是2
# 推荐如下：
# 0 -> 2（共同好友：1）
# 1 -> 3（共同好友：2）
# 2 -> 0（共同好友：1）
# 3 -> 1（共同好友：2）
expected = [2, 3, 0, 1]


def recommend(n: int, edges: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(n)]
    for v, w in edges:
        adj[v].append(w)
        adj[w].append(v)

    res = [-1] * n

    for root in range(n):
        q = [root]
        vis = [False] * n
        vis[root] = True
        cnt = [0] * n
        first_level = set()

        depth = 0
        while q:
            level_size = len(q)

            for _ in range(level_size):
                node = q.pop(0)
                first_level.add(node)

                for w in adj[node]:
                    if depth == 1 and w not in first_level:
                        cnt[w] += 1

                    if vis[w]:
                        continue
                    
                    vis[w] = True
                    q.append(w)

            if depth == 1:
                break
            depth += 1

        if root == 3: print(cnt)
        mx = cnt[0]
        mi = 0
        for i, v in enumerate(cnt):
            if v > mx:
                mx = v
                mi = i
        res[root] = mi if mx > 0 else -1


    return res


def test_recommend():
    test_cases = [
        # (users, edges, expected)
        # ([0, 1, 2, 3], [[0, 1], [1, 2], [2, 3]], [2, 3, 0, 1]),
        # ([0, 1, 2], [[0, 1], [1, 2], [0, 2]], [-1, -1, -1]),
        # ([0, 1, 2, 3], [[0, 1], [1, 2]], [2, -1, 0, -1]),
        # ([0, 1, 2, 3], [[0, 1], [1, 2], [1, 3], [0, 3], [2, 3]], [2, -1, 0, -1]),
        ([0, 1, 2, 3, 4], [[0, 1], [0, 2], [2, 3], [1, 3], [3, 4]], [3,2,1,0,1]),
        # ([0], [], [-1]),
    ]

    for i, (users, edges, expected) in enumerate(test_cases):
        result = recommend(len(users), edges)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")


# 调用测试函数（前提是你已经实现了 recommend 函数）
test_recommend()
