from collections import deque
class Graph:
    def __init__(self):
        self.graph={}
    def addvertex(self,v1):
        if v1 not in self.graph:
            self.graph[v1]=[]
    def addedges(self,v1,v2,isdirected=False):
        self.addvertex(v1)
        self.addvertex(v2)
        self.graph[v1].append(v2)
        if not isdirected:
            self.graph[v2].append(v1)
    def short(self,start,end):
        visited=set()
        queue=deque([(start,[start])])
        while queue:
            node,path=queue.popleft()
            if node==end:
                return path
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,path+[neighbor]))
        return None
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}->{value}")
g=Graph()
g.addedges('A','B')
g.addedges('B','C')
g.addedges('C','D')
g.display()
print(g.short('A','C'))            