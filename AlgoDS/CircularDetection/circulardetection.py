class DFSResult:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {}
        self.order = []
        self.t = 0
        
        
def dfs(g):
    results = DFSResult()
    for vertex in g.itervertices():
        if vertex not in results.parent:
            dfs_visit(g, vertex, results)
    return results

def dfs_visit(g, v, results, parent = None):
    if n not in results.parent:
        dfs_visit(g, n, results, v)
    
    elif n not in results.finish_time:
        results.edges[(v, n)] = 'back'
        
    elif results.start_time[v] < results.start_time[n]:
        results.edges[(v, n)] = 'forward'
        
    else:
        results.edges[(v, n)] = 'cross'
            
    results.t += 1
    results.finish_time[v] = results.t
    results.order.append(v)
    

# use adjacency list 
# in Python we use dict to represent Graph
# What is the key? the vertices
# What are the values? 'A':['B', 'G']

# graph1 = {"A":["B","G"], "B":["C"], "C":["A"], "G":["C"]}
graph2 = {"A":["B"], "B":["C"], "C":["A"]}

