def winner(scores):
  top = 0
  maxx = -10**10
  for i in range(len(scores)):
    if maxx < scores[i]:
      top = i + 1
      maxx = scores[i]
  return top

def average(scores):
  if len(scores) = 0:
    return 0.0

  summ = 0
  for n in scores:
    summ += n
  
  return summ / len(scores)


def ranking(scores, names):
  nm = names.copy()
  return sorted(nm, key=lambda n: -scores[names.index(n)])

  
  def above_average(names, scores, avr):
    nm = []
    for i in range(len(scores)):
      if scores[i] > avr:
        nm.append(names[i])
    return nm
    
    
    


names = list(input())
scores = list(input())
