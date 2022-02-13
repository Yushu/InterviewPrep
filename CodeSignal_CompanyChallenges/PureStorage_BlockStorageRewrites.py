from itertools import groupby, accumulate

def createBlocks(num_writes, threshold):
  i = 0
  for key, group in groupby(num_writes, lambda x : x >= threshold):
    # This is faster compared to len(list(g))
    length = sum(1 for _ in group)
    if key:
      yield [i, i + length - 1]
    i += length

def createWrites(block_count, writes):
  tot_writes = dict(enumerate([0] * (block_count + 1)))
  for lower, upper in writes:
    tot_writes[lower] += 1
    tot_writes[upper + 1] -= 1
  return list(accumulate(tot_writes.values()))

def blockStorageRewrites(blockCount, writes, threshold):
  num_writes = createWrites(blockCount, writes)
  return list(createBlocks(num_writes, threshold))

blockCount1 = 10
writes1 = [[0, 4], [3, 5], [2, 6]]
threshold1 = 2
#[[2,5]]
blockCount2 = 10
writes2 = [[3,4], [0,1], [6,6]]
threshold2 = 1
#[[0,1], [3,4], [6,6]]

print(blockStorageRewrites(blockCount1, writes1, threshold1))
print()
print(blockStorageRewrites(blockCount2, writes2, threshold2))