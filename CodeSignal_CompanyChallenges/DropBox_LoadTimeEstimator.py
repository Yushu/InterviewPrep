def loadTimeEstimator(sizes, uploadingStart, v):
  result = [x for x in uploadingStart]
  t = [0 for x in uploadingStart]
  c = len(sizes)
  _time = 0
  curr_time = uploadingStart[0]
  while (c > 0):
    up_start_idx = [i for i, x in enumerate(uploadingStart) if x == curr_time + _time and sizes[i] != 0 ]

    if len(up_start_idx):
      speed = v/float(len(up_start_idx))
    else:
      speed = v

    for i in up_start_idx:
      if sizes[i] > 0:
        sizes[i] = sizes[i] - speed
        result[i] = result[i] + 1
        t[i] = t[i] + 1

      uploadingStart[i] = uploadingStart[i] + 1
    _time += 1
    c = len([x for x in sizes if x > 0])
  return result
  
print(loadTimeEstimator([21, 10], [100,105],2))
print(loadTimeEstimator([20, 10], [1, 1], 1))
print(loadTimeEstimator([1, 1, 1], [10, 20, 30], 3))