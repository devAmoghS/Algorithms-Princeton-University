# Eager implementation of the Quick Find algorithm
# Problem: Dynamic Connectivity

# ** Peformance
# 1. is_connected: takes constant time - O(1)
# 2. union: takes quadratic time - O(N^2)

class QuickFindUF:
  def __init__(self, arr, size):
    self.arr = [i for i in range(0, size)]

  def is_connected(self, p, q):
    array = self.arr
    return array[p] == array[q] 

  def union(self, p, q):
    array = self.arr
    p_id = array[p]
    q_id = array[q]

    for i in array:
      if i == p_id:
        i = q_id
