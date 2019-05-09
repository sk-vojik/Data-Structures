class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    pass

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
    # loop until either the element reaches the end of the array
    # or we'll break the loop
    while index > 0:
      left_child = (2 * index) + 1
      right_child = (2 * index) + 2
      if self.storage[left_child] > self.storage[right_child] and self.storage[left_child] > self.storage[index]:
        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
      elif self.storage[right_child] > self.storage[left_child] and self.storage[right_child] > self.storage[index]:
        self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
      else:
        break
