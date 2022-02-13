def coverDebts(s, debts, interests):
  zipped = list(zip(interests, debts))
  zipped.sort(reverse=True)
  n = len(zipped)
  min_amount_req = 0
  for i in range(len(debts)):
    zipped[i] = list(zipped[i])
  while True:
    amount = s*0.1
    isEmpty = True
    for i in range(n):
      if zipped[i][1] > 0:
        isEmpty = False
        if zipped[i][1] > amount:
          zipped[i][1] -= amount
          min_amount_req += amount
          break
        else:
          amount -= zipped[i][1]
          min_amount_req += zipped[i][1]
          zipped[i][1] = 0
    if isEmpty:
      break
    else:
      for i in range(n):
        if zipped[i][1] > 0:
          zipped[i][1] += zipped[i][1]*(zipped[i][0]*0.01) 
  return min_amount_req

s1 = 50
debts1 = [2, 2, 5]
interests1 = [200, 100, 150]

s2 = 40
debts2 = [2, 2, 5]
interests2 = [75, 25, 25]

print(coverDebts(s1, debts1, interests1))
print()
print(coverDebts(s2, debts2, interests2))