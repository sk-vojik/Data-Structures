class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    current = self.storage.pop(0)
    self._sift_down(0)
    return current

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  #The index parameter is the index of the node wherever it is in the array
  def _bubble_up(self, index):
    # loop until the element is at the top, or break when we realize element is smaller than parent
    while index > 0:
      parent = (index - 1) // 2
      #check if the element at index has a higher priority than the parent 
      if self.storage[index] > self.storage[parent]:
        #if so, swap em
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        #we also need to update the index
        index = parent
      
      #otherwise, element has reached its right place - stop climbing
      else:
        break
      

  def _sift_down(self, index):
    while index  * 2 + 1 <= len(self.storage) - 1:
      if (index * 2) + 2 > len(self.storage) - 1:
        biggest = (index * 2) + 1
      elif self.storage[(index * 2) + 1] > self.storage[(index * 2) + 2]:
        biggest = (index * 2) + 1
      else:
        biggest = (index * 2) + 2
      
      if self.storage[biggest] > self.storage[index]:
        current = self.storage[biggest]
        self.storage[biggest] = self.storage[index]
        self.storage[index] = current
      index = biggest
