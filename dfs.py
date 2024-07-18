visited = set()  
def dfs(visited, graph, node):             
    if node not in visited:                 
        print(node, end='->' if node != node[-1] else " " )   
        visited.add(node)                   
        for neighbour in graph[node]:       
            dfs(visited, graph, neighbour) 

graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

print("Following is the Depth-First Search")
dfs(visited, graph, '5')
