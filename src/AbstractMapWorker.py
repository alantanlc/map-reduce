from abc import ABC, abstractmethod
import AbstractWorker

class AbstractMapWorker(AbstractWorker):

  def __init__(self):
    self.input_filename = None
    self.intermediate_filename = None

  def execute(self):
    self.map()

  @abstractmethod
  def map(self):
    pass
