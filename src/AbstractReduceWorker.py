from abc import ABC

def AbstractReduceWorker(ABC):

  def __init__(self):
    self.output_file = None

  def execute(self):
    self.reduce()

  @abstractmethod
  def reduce(self):
    pass
