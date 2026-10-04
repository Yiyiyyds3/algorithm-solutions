import sys
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return  
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
    
    def count_sets(self):
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return len(roots)

def min_rooms(n, friendships):
    uf = UnionFind(n)
    
    for a, b in friendships:
        uf.union(a, b)
    
    return uf.count_sets()

if __name__ == "__main__":
    num=int(input())
    for _ in range(num):
        n,m=map(int,input().split())
        friendships=[]
        for i in range(m):
            a,b = map(int, input().split())
            friendships.append((a,b))
        print(min_rooms(n+1, friendships)-1)