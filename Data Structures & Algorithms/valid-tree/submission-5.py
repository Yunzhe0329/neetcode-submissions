class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree -> no cycles, full connected
        if len(edges) < (n - 1):
            return False
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def DFS(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not DFS(nei, node):
                    return False
            return True
        return DFS(0, -1) and len(visited) == n
