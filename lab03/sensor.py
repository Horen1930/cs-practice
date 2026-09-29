top = float((input()))
n = int(input())
cnt_error = 0
cnt_top = 0
maxx = -10**10
cnt = 0
summ = 0

for _ in range(n):
    
    t = input()

    if t == 'error':
        cnt_error += 1
        continue

    t = float(t)
    cnt += 1
    summ += t

    maxx = max(maxx, t)

    if t > top:
         cnt_top += 1

avarage = summ / cnt if cnt > 0 else 0

print(f"{n}\n{cnt_error}\n{cnt_top}\n{maxx:.1f}\n{avarage:.1f}")