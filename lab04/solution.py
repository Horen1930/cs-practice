def winner(scores):
  top = 0
  maxx = -10**10
  for i in range(len(scores)):
    if maxx < scores[i]:
      top = i + 1
      maxx = scores[i]



names = list(input());
scores = list(input());
