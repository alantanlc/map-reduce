from abc import ABC, abstractmethod

def AbstractReduceWorker(AbstractWorker):

  def __init__(self):
    self.output_file = None

  def execute(self):
    self.reduce()

  @abstractmethod
  def reduce(self):
    pass
