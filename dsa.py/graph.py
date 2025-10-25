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
        visited=set([start])
        queue=deque([(start,[start])]) #current node,path taken to reach the node
        while queue:
            node,path=queue.popleft()
            if node==end:
                return path
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,path+[neighbor]))
        return None
    
    def is_cyclic(self):
        visited=set()
        recursion_stack=set()
        def dfs(node):
            visited.add(node)
            recursion_stack.add(node)
            for nei in self.graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                elif nei in recursion_stack:
                    return True
            recursion_stack.remove(node)
            return False
        for node in self.graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False   
                 
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}->{value}")
g=Graph()
g.addedges('A','B')
g.addedges('B','C')
g.addedges('C','D')
g.display()
print(g.short('A','C')) 
print(g.is_cyclic())  
         

class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rx,ry=self.find(x),self.find(y)
        if rx!=ry:
            if self.rank[x]<self.rank[y]:
                self.parent[rx]=y
            elif self.rank[x]>self.rank[y]:
                self.parent[ry]=x
            else:
                self.parent[y]=x
                self.rank[x]+=1
            return True
        return False
def kruskal(n,edges):
    edges.sort(key=lambda x:x[2])
    dsu=DSU(n)
    mst_edges=[]
    mst_weight=0
    num_edges_mst=0
    for u,v,weight in edges:
        if dsu.union(u,v):
            mst_edges.append((u,v,weight))
            mst_weight+= weight
            num_edges_mst+=1
            if num_edges_mst==n-1:
                break
    return mst_edges,mst_weight
n=4
edges = [
        (0, 1, 10),
        (1, 3, 15),
        (2, 3, 4),
        (2, 0, 6),
        (0, 3, 5)
    ]
print(kruskal(4,edges))
        