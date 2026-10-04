import sys
def find_best_resolution(w1,h1):
    min_distance = float('inf')
    best_w2 = None
    best_h2 = None
    start_k = max(1, (w1 // 4) - 10)
    end_k = (w1 // 4) + 10
    for k in range(start_k, end_k + 1):
        w2 = 4 * k
        h2 = 3 * k
        distance = abs(w2 - w1) + abs(h2 - h1)
        
        if distance < min_distance:
            min_distance = distance
            best_w2 = w2
            best_h2 = h2
    return best_w2, best_h2
# nums=list()
# for i in range(1,4001):
#     for j in range(1,3001):
#         if i/j==4/3:
#             nums.append((i,j))
#             break
# print(nums[0][0],nums[0][1])

for i in sys.stdin:
    w,h=map(int,i.split())
    w3,h3=find_best_resolution(w,h)
    print(w3,h3) 
    
