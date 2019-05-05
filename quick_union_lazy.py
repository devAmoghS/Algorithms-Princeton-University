# Lazy implementation of the Quick Union algorithm
# Problem: Dynamic Connectivity

# ** Peformance
# 1. is_connected: takes linear time - O(N)
# 2. union: takes linear time - O(N)

class QuickUnionUF:
  def __init__(self, arr, size):
    self.arr = [i for i in range(0, size)]

  def root(self, i):
    array = self.arr
    while array[i] != i:
      i = array[i]
    return i

  def is_connected(self, p, q):
    return root(p) == root(q) 

  def union(self, p, q):
    array = self.arr
    i = root(p)
    j = root(q)

    array[i] = j
