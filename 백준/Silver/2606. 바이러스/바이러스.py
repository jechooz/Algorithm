def dfs(computer, graph, visited):
    visited[computer] = True  
    for connected_computer in graph[computer]:  
        if not visited[connected_computer]: 
            dfs(connected_computer, graph, visited)

n = int(input()) 
m = int(input()) 
graph = [[] for _ in range(n + 1)]  

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)
dfs(1, graph, visited)

result = sum(visited) - 1 
print(result)