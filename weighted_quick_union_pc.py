class WeightedQuickUnionPathCompression:
  def __init__(self, arr, count):
    self.arr = [i for i in range(0, count)]
    self.sz = [0] * count 

  def root(self, i):
    array = self.arr
    while array[i] != i:
      array[i] = array[array[i]] # pointing to grandparent
      i = array[i]
    return i

  def is_connected(self, p, q):
    return root(p) == root(q) 

  def union(self, p, q):
    array = self.arr
    size = self.sz

    i = root(p)
    j = root(q)

    if i == j:
      return
    elif size[i] < size[j]:
      array[i] = j
      size[j] += size[i]
    else:
      array[j] = i
      size[i] += i
