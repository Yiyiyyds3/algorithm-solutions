import sys
#使用递推比递归要快的多
def generate_pascal(n):
    row = [1] 
    for i in range(n):
        print(' '.join(map(str, row)))
        next_row = [1]
        for j in range(1, i + 1):
            next_row.append(row[j-1] + row[j])
        next_row.append(1)
        row = next_row

for line in sys.stdin:
    line = line.strip()
    n = int(line)
    if n == 0:
        break
    generate_pascal(n)
    print() 
