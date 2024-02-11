class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(source):
            if source == destination:
               return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)
        
