class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check if the new node's value is less than the current node's value
    if value < self.value:
      #check if there is no left child
      if not self.left:
        self.left = BinarySearchTree(value)
      # if there is a left, keep goin down
      else:
        self.left.insert(value)
    # do the same on the right side if the node's value >= the current node's value
    else:
      #check if there is no right child
      if not self.right:
        #park value here
        self.right = BinarySearchTree(value)
      else:
        #keep recursing down to the right since there is a right child
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)


  def get_max(self):
    if not self.right:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)