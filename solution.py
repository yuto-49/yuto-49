import sys
from collections import defaultdict


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0

    def rd():
        nonlocal idx
        v = int(data[idx])
        idx += 1
        return v

    MOD = 10**9 + 7
    n, q = rd(), rd()

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = rd(), rd()
        adj[u].append(v)
        adj[v].append(u)

    # Compute parent, depth, euler tour via iterative DFS
    par = [0] * (n + 1)
    dep = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)

    timer = 0
    stk = [(1, 0, False)]
    while stk:
        nd, p, leaving = stk.pop()
        if leaving:
            tout[nd] = timer - 1
            continue
        par[nd] = p
        dep[nd] = dep[p] + (1 if p else 0)
        tin[nd] = timer
        timer += 1
        stk.append((nd, p, True))
        for v in adj[nd]:
            if v != p:
                stk.append((v, nd, False))

    # Binary lifting for LCA
    LOG = max(1, n.bit_length())
    up = [[0] * (n + 1) for _ in range(LOG)]
    for v in range(1, n + 1):
        up[0][v] = par[v]
    for k in range(1, LOG):
        for v in range(1, n + 1):
            up[k][v] = up[k - 1][up[k - 1][v]]

    def lca(u, v):
        if dep[u] < dep[v]:
            u, v = v, u
        d = dep[u] - dep[v]
        for k in range(LOG):
            if (d >> k) & 1:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    def is_anc(u, v):
        return tin[u] <= tin[v] and tout[v] <= tout[u]

    out = []

    for _ in range(q):
        k = rd()
        nodes = [rd() for __ in range(k)]

        if k <= 1:
            out.append('0')
            continue

        nodes.sort(key=lambda x: tin[x])

        # Collect key nodes: query nodes + LCAs of consecutive pairs
        key = set(nodes)
        for i in range(len(nodes) - 1):
            key.add(lca(nodes[i], nodes[i + 1]))

        all_nd = sorted(key, key=lambda x: tin[x])

        # Build virtual tree using stack
        children = defaultdict(list)
        s = [all_nd[0]]
        for i in range(1, len(all_nd)):
            v = all_nd[i]
            while len(s) > 1 and not is_anc(s[-1], v):
                s.pop()
            children[s[-1]].append(v)
            s.append(v)

        # Compute answer using edge contributions
        query_set = set(nodes)
        total = sum(nodes) % MOD

        sub = {}
        for nd in all_nd:
            sub[nd] = nd % MOD if nd in query_set else 0

        ans = 0

        # Iterative post-order DFS on the virtual tree
        dfs = [(all_nd[0], False)]
        while dfs:
            v, done = dfs.pop()
            if done:
                for c in children[v]:
                    w = dep[c] - dep[v]
                    ans = (ans + w * sub[c] % MOD * ((total - sub[c]) % MOD)) % MOD
                    sub[v] = (sub[v] + sub[c]) % MOD
                continue
            dfs.append((v, True))
            for c in children[v]:
                dfs.append((c, False))

        out.append(str(ans % MOD))

    sys.stdout.write('\n'.join(out) + '\n')


main()
