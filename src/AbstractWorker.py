from abc import ABC

class AbstractWorker(ABC):

  def __init__(self, storage_dir):
    self.storage_dir = storage_dir # storage
    self.data = None

  @abstractmethod
  def assign(self, file_name):
    pass

  @abstractmethod
  def execute(self):
    pass

