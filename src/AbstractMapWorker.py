from abc import ABC

class AbstractMapWorker(ABC):

  def __init__(self):
   self.input_filename = None
    self.intermediate_filename = None

  def execute(self):
    self.map()

  @abstractmethod
  def map(self):
    pass
