from collections import defaultdict

def cycle_exists(G):                     # - G is a directed graph
    color = defaultdict(str)
    
    for u in G:
        color[u] = "white"
    
    # color = { u : "white" for u in G  }  # - All nodes are initially white
    found_cycle = [False]                # - Define found_cycle as a list so we can change
    
    print color
    print color['dafa']
                                         # its value per reference, see:
                                         # http://stackoverflow.com/questions/11222440/python-variable-reference-assignment
    for u in G:                          # - Visit all nodes.
        if color[u] == "white":
            dfs_visit(G, u, color, found_cycle)
        if found_cycle[0]:
            break
    return found_cycle[0]
 
#-------
 
def dfs_visit(G, u, color, found_cycle):
    if found_cycle[0]:                          # - Stop dfs if cycle is found.
        return
    color[u] = "gray" 
    # - Gray nodes are in the current path
    for v in G[u]:   
        print "sth"
        # - Check neighbors, where G[u] is the adjacency list of u.
        # if color[v] == "gray":                  # - Case where a loop in the current path is present.  
        #     found_cycle[0] = True       
        #     return
        # if color[v] == "white":                 # - Call dfs_visit recursively.   
        #     dfs_visit(G, v, color, found_cycle)
            
    color[u] = "black"                          # - Mark node as done.
    
    
    
# graph_example_1 = { 0 : [1],
#                     1 : [2],
#                     2 : [3],
#                     3 : [4],
#                     4 : [1] }

graph_example_2 = {u'a': [u'xxxxxxxxx'], 
                   u'c': [u'xxx', u'b', u'xxxx'], 
                   u'b': [u'x', u'c', u'xx']}

# try:                    
print cycle_exists(graph_example_2)
# except KeyError:
#     print "KeyErrorHandled"