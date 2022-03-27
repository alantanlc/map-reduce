from abc import ABC

class AbstractWorker(ABC):

  @abstractmethod
  def assign(self, file_name):
    pass

  @abstractmethod
  def execute(self):
    pass

  @abstractmethod
  def read(self):
    pass

  @abstractmethod
  def emit(self):
    pass
