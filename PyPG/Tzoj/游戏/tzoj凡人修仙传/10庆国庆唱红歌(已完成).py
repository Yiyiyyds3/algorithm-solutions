import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        m, n = map(int, line.split())
    except ValueError:
        continue
    
    if m == 0 and n == 0:
        break
    
    # ✅ 用推导式创建独立的二维数组（只分配需要的大小）
    nums = [[0] * n for _ in range(m)]
    
    total_people = 0  # 实际有人的数量
    blocked = 0       # 被挡住的人数
    
    # 读入数据，同时统计总人数
    for i in range(m):
        row_line = sys.stdin.readline().strip()
        if not row_line:
            continue
        try:
            nums[i] = list(map(int, row_line.split()))
            for h in nums[i]:
                if h > 0:
                    total_people += 1
        except ValueError:
            continue
    
    # 判断被挡住的人数（跳过空座位）
    for j in range(n):
        prev_height = 0  # 记录这一列前面的最高人（从第一排开始）
        for i in range(m):
            curr = nums[i][j]
            if curr == 0:
                continue  # 空座位，跳过
            if prev_height > curr:
                blocked += 1
            if curr > prev_height:
                prev_height = curr  # 更新这一列的最高高度
    
    # 输出（注意：题目保证不会所有位置为空，所以total_people>0）
    print(f"{blocked / total_people * 100:.1f}%")