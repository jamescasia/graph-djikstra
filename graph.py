import math
class Node:
    def __init__(self,id, value = None):
        self.value = value
        self.id = id
    def __str__(self):
        return "(" + str(self.id) + ")"

class Edge:
    def __init__(self, start, dist, end):
        self.start = start
        self.dist = dist
        self.end = end

class Graph:
    def __init__(self, edges={}, nodes = {}):
        # { 0: [Edge]}
        self.edges = edges
        # { 0: Node}
        self.nodes = nodes
    def addNode(self, value):
        # self.nodes[len(self.nodes)] = Node(id = len(self.nodes),value = value)
        self.nodes[value] = Node(id = value,value = value)
    def addEdge(self, startId, dist, endId):
        if startId in self.edges:
            self.edges[startId].append(Edge(startId, dist, endId))
            
        else:
            self.edges[startId] = [Edge(startId, dist, endId)]  

        if endId in self.edges:
            self.edges[endId].append(Edge(endId, dist, startId))
        else:
            self.edges[endId] = [Edge(endId, dist, startId)]  

    def shortestPath(self, startId, endId):
        # based on Geeks for Geeks
        sptSet = set([])
        # sptSet = { nodeId}
        # 1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path
        #  tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
        distances = {}
        # {nodeId: distance}
        # 2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE.
        #  Assign distance value as 0 for the source vertex so that it is picked first.
        for k in self.nodes.keys():
            if(k == startId):
                distances[k] = 0
            else:
                distances[k] = math.inf 
 
        # While sptSet doesn’t include all vertices
        while len(list(sptSet)) != len(self.nodes): 
 
            temp = {}
            for k, dist in distances.items():
                if(k not in sptSet):
                    temp[k] = dist 
            # Pick a vertex u which is not there in sptSet and has minimum distance value.
            u = min(temp, key=distances.get)
            #   Include u to sptSet.
            sptSet = sptSet.union({u}) 
            # Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. 
            # For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, 
            # then update the distance value of v.
            for edge in self.edges[u]:
                if(distances[u]+edge.dist  <distances[edge.end]):
                    distances[edge.end] = distances[u]+edge.dist
        print(distances)
        return distances[endId]



        
         


        pass
    def __str__(self):
        print("nodes:\n", " ".join([str( self.nodes[n]) for n in self.nodes]))
        for key in self.nodes:
            node = self.nodes[key]
            print(node.id)
            if(node.id in self.edges):
                for edge in self.edges[node.id]:
                    
                    
                    print("  --"+ str(edge.dist) +"-->" , str(self.nodes[edge.end]))
        return ""
        # currNode = 
graph = Graph()

for i in range(9):
    graph.addNode(i)


graph.addEdge(0,4,1)
graph.addEdge(0,8,7)  

graph.addEdge(1,8,2)
graph.addEdge(1,11,7)  

graph.addEdge(2,7,3)
graph.addEdge(2,4,5)  
graph.addEdge(2,2,8)  

graph.addEdge(3,9,4)
graph.addEdge(3,14,5)  
 
graph.addEdge(4,10,5)  
 
graph.addEdge(5,2,6) 
 
graph.addEdge(6,6,8)
graph.addEdge(6,1,7)  
 
graph.addEdge(7,7,8)  


print(graph)
print(graph.shortestPath(0,8))