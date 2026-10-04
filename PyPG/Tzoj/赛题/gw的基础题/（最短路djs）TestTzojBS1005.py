import heapq
import sys
input=sys.stdin.readline
# 1. 构建邻接表
def dijkstra(n, start):
    # 1. 初始化距离数组
    # dist[i] 表示起点到 i 的最短距离
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    
    # 2. 初始化优先队列（最小堆）
    # 元素格式：(当前距离, 节点编号)
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # 如果这个距离已经不是最新的了，跳过（剪枝）
        if current_dist > dist[u]:
            continue
            
        # 3. 遍历节点 u 的所有邻居
        for v, w in adj[u]:
            # 4. 松弛操作
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    adj=[[] for i in range(n+1)]
    for j in range(m):
        u,v,w=map(int,input().split())
        adj[u].append((v,w))
        adj[v].append((u,w))
    result = dijkstra(n, 1)
    if result[n] == float('inf'):
        print("NO")
    else:
        print(result[n])    