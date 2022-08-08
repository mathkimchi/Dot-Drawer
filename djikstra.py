class Graph:
    def __init__(self, nodes=[]):
        self.nodes=nodes
        self.edges=dict()

    def createNode(self, **kwargs):
        node=Node(self, **kwargs)
        self.nodes.append(node)
        return node

    def createUniEdge(self, edge, edgeData):
        '''
        type edge: tuple cus sets aren't hashable 
        ex: (nodeStart, nodeEnd)
        
        type edgeData: dict
        ex: {'dist':5, 'Too early for weird jokes':'always'}
        '''
        self.edges[edge]=edgeData
        #update edges for the nodes
        edge[0].children.append(edge[1])


    def createBiEdge(self, edge, edgeData):
        self.createUniEdge(edge, edgeData)
        self.createUniEdge((edge[1], edge[0]), edgeData)



class Node:
    def __init__(self, graph, val=None, children=[]):
        self.graph=graph
        self.val=val
        self.children=children[:] #list of just all the edges. can find edgeData w/ self.graph.edges[(self, child)]
        # why does adding a child for one node add for all nodes without the [:] in the prev line?



def dijkstra(nodeA, graph):
    dists={node:4095 for node in graph.nodes}
    dists[nodeA]=0
    unvisited=[node for node in graph.nodes] #treat like never sorted
    trail=[nodeA]
    # edgeLengths={} #I don't think this is important
    # for edge in graph.edges:
    #     edgeLengths[edge]=graph.edges[edge]['dist']

    while len(unvisited)>0:
        cUnv=min(unvisited, key=lambda node: dists[node]) #closest unvisited, just the node
        for tNode in cUnv.children: #touchingNode
            dists[tNode]=min(dists[tNode], dists[cUnv]+graph.edges[(cUnv, tNode)]['dist']) #0 is distance alr set, 1 is cUnv's distance+dist from cUnv to tNode
        unvisited.remove(cUnv)
    return dists



graph=Graph()
node0=graph.createNode(val="A")
node1=graph.createNode(val="B")
node2=graph.createNode(val="C")
node3=graph.createNode(val="D")
node4=graph.createNode(val="E")
graph.createBiEdge((node0, node1), {'dist':5})
graph.createBiEdge((node0, node2), {'dist':10})
graph.createBiEdge((node0, node3), {'dist':3})
graph.createBiEdge((node0, node4), {'dist':15})
graph.createBiEdge((node1, node2), {'dist':2})
graph.createBiEdge((node1, node3), {'dist':1})
graph.createBiEdge((node2, node4), {'dist':2})
graph.createBiEdge((node3, node4), {'dist':7})
distances=dijkstra(node0, graph)
for d in distances.items():
    print(d[0].val, d[1])