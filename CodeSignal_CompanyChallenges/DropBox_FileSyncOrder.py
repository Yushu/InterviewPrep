from heapq import heappop, heappush

def fileSyncOrder(files, storageLimit, uploadSpeed, duration):
  used, stored = 0, 0
  result = []

  files = [(x[0], x[1], i) for i, x in enumerate(files)]       
  while files:
    temp = [x for x in files if x[1] <= used]
    if not temp:
      temp = sorted(files, key=lambda x: (x[1], x[0]))
    else:
      temp = sorted(temp, key=lambda x: (x[0], x[1]))
    for el in temp:
      _size, _time, _index = el
      if _time > used:
        used = _time
      _delta_size = _size + stored
      _dela_time = float(_size) / uploadSpeed + used
      files.remove(el)
      if _delta_size <= storageLimit and _dela_time <= duration:
        stored += _size
        used += float(_size) / uploadSpeed
        result.append(_index)
        break
  return result

  
print(fileSyncOrder([[10, 5],[10, 7],[8, 10],[2, 20]], 20, 2, 100))
#Expected o/p: [0, 2, 3]

print(fileSyncOrder([[10, 5]], 100, 1, 10))
#Expected o/p: []