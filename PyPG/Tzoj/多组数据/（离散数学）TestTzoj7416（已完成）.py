import sys
for line in sys.stdin:
    line = line.strip()
    fps, hp = map(int, line.split())
    hp -= 1
    ans = hp // (2 * fps)
    if hp % (2 * fps) >= fps:
        ans += 1
    print(ans)