n, m = map(int,input().split())
spec = []
for i in range(n):
    spec.append(set())
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        if a[j] == 1:
            spec[i].add(j)
ans = 10000000
for p1 in range(m):
    for p2 in range(p1+1, m):
        one = 0
        two = 0
        three = 0
        four = 0
        for i in range(n):
            if p1 in spec[i] and p2 in spec[i]:
                one += 1
            elif p1 in spec[i] and p2 not in spec[i]:
                two += 1
            elif p1 not in spec[i] and p2 in spec[i]:
                three += 1
            else:
                four += 1
        x = max([one,two,three,four])
        if x < ans:
            ans = x
            ans_1 = p1
            ans_2 = p2
print(ans)
print(ans_1+1, ans_2+1)