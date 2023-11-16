# def build_graph():
#     graph = {}
#     n = int(input("Enter the number of vertices: "))
#     for i in range(n):
#         vertex = input(f"Enter vertex {i + 1}: ")
#         adjacent_vertices = input(f"Enter adjacent vertices for {vertex} (comma-separated): ").split(',')
#         graph[vertex] = [v.strip() for v in adjacent_vertices]
#     return graph

# def dfs_recursive(graph, node, visited):
#     if node not in visited:
#         print(node, end=' ')
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs_recursive(graph, neighbor, visited)

# def dfs(graph):
#     visited = set()
#     for node in graph:
#         if node not in visited:
#             dfs_recursive(graph, node, visited)

# def bfs_recursive(graph, queue, visited):
#     if not queue:
#         return
#     node = queue.pop(0)
#     if node not in visited:
#         print(node, end=' ')
#         visited.add(node)
#         queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# def bfs(graph):
#     visited = set()
#     for node in graph:
#         if node not in visited:
#             queue = [node]
#             bfs_recursive(graph, queue, visited)

# # Creating the graph based on user input
# graph = build_graph()

# # Running DFS
# print("\nDFS:")
# dfs(graph)

# # Running BFS
# print("\nBFS:")
# bfs(graph)


def create_graph():
    graph={}
    n=int(input("ENter the number of vertices"))
    for i in range(n):
        vertex=input(f"Enter the {i+1}")
        adj_vertex=input(f"Enter the adjacent vertex for {vertex} in coomma separeted form ".split(','))
        graph[vertex]=[v.strip() for v in adj_vertex]
    return graph

graph=create_graph()
def dfs_recursive(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph,neighbor,visited)
def dfs(graph):
    visited=set()
    for node in graph: 
        if node not in visited:
            dfs_recursive(graph,node,visited) 
dfs(graph)  


def bfs_recursive(graph,queue,visited):
    if not queue:
        return
    node=queue.pop(0)
    if node not in visited:
        print(node,end='')
        visited.add(node)
        queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
def bfs(graph):
    visited=set()
    for node in graph:
        if node not in visited:
            queue=[node]
            bfs_recursive(graph,queue,visited)
bfs(graph)
