from abc import ABC, abstractmethod
import AbstractWorker
import pdb

class AbstractMapWorker(AbstractWorker):

  def __init__(self, storage_dir):
    self.input_filename = None
    self.intermediate_filename = None
    super().__init__(storage_dir)

  def assign(self, input_filename, intermediate_filename):
    self.input_filename = input_filename # input-*.txt
    self.intermediate_filename = intermediate_filename # intermediate-*.txt

  def execute(self):
    self.map()
    self.emit()

  @abstractmethod
  def map(self):
    pass

  @abstractmethod
  def emit(self):
    pass
