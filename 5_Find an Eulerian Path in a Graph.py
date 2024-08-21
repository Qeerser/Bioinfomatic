def dfs(pre_node, node, graph, path, visited):
    visited.add((pre_node, node))
    if node in graph:
        for next_node in graph.get(node, [])[::-1]:
            if (node, next_node) not in visited:  
                dfs(node, next_node, graph, path, visited)
    path.append(node)

def find_longest_path(graph,start):
    first_value = next(iter(graph))
    if start == 0 :start = first_value
    
    visited = set()
    path = []
    dfs("-1", start, graph, path, visited, )
    return path

def count_net_degrees(graph):

    net_degrees = {}
    for vertex in graph:
        net_degrees[vertex] = net_degrees.get(vertex, 0) + len(graph[vertex])
        for neighbor in graph[vertex]:
            net_degrees[neighbor] = net_degrees.get(neighbor, 0) - 1
        
    return net_degrees

graph = {}
with open("input.txt", 'r') as file:
    for line in file:
        node, path = line.strip().split(" -> ")
        next_nodes = path.strip().split(",")
        graph[node] = next_nodes

net_degrees = count_net_degrees(graph)
start = 0
for key,i in net_degrees.items():
    if (i == 1): 
        start = key
        break

longest_path = find_longest_path(graph,start)

with open("output.txt", 'w') as output_file:
    output_file.write('->'.join(longest_path[::-1]))