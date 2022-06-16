from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def insertEdge(self,v1,v2):
        self.graph[v1].append(v2)
        
    def printGraph(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(i,"=>",j)
g=Graph()

g.insertEdge(1,5)
g.insertEdge(5,2)
g.insertEdge(2,7)
g.insertEdge(7,1)

g.printGraph()

#1=>5
#5=>2
#2=>7
#7=>1
