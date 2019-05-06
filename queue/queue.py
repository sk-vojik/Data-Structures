class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we 
    # use to store queue elements?
    self.storage = list()

  def enqueue(self, item):
    self.storage.insert(0, item)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop()
    return None

  def len(self):
    return self.size
