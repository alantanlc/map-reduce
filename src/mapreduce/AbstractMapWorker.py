from abc import abstractmethod
from mapreduce.AbstractWorker import AbstractWorker
import os

class AbstractMapWorker(AbstractWorker):

  def __init__(self):
    self.input_dir = 'input'
    self.intermediate_dir = 'intermediate'
    self.input_filename = None
    self.intermediate_filename = None
    self.result = {}

  def assign(self, storage_dir, input_filename, intermediate_filename):
    self.storage_dir = storage_dir # ../storage
    self.input_filename = input_filename # input-*.txt
    self.intermediate_filename = intermediate_filename # intermediate-*.txt

  def get_input_filename(self):
    return os.path.join(self.storage_dir, self.input_dir, self.input_filename)

  def get_intermediate_filename(self):
    return os.path.join(self.storage_dir, self.intermediate_dir, self.intermediate_filename)

  # Overridden method
  def execute(self):
    self.reset()
    self.map()
    self.emit()

  def reset(self):
    self.result = {}

  @abstractmethod
  def map(self):
    pass

  def emit(self):
    # Write result to intermediate file
    with open(self.get_intermediate_filename(), 'w') as f:
      for key, value in self.result.items():
        f.write(f'{key},{value}\n')

