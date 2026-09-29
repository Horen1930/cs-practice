top = float((input()))
n = int(input())
cnt_error = 0
cnt_hight = 0
maxx = -10**10
cnt = 0
summ = 0

for _ in range(n):

    t = input()

    if t == 'error':
        cnt_error += 1
        continue

    t = float(t)