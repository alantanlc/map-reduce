from abc import ABC, abstractmethod

class AbstractWorker(ABC):

  def __init__(self):
    self.storage_dir = None

  @abstractmethod
  def execute(self):
    pass

