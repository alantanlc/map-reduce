from abc import abstractmethod
from mapreduce.AbstractWorker import AbstractWorker
import os

class AbstractReduceWorker(AbstractWorker):

  def __init__(self):
    self.intermediate_dir = 'intermediate'
    self.output_dir = 'output'
    self.intermediate_filenames = None
    self.output_filename = None
    self.key = None
    self.result = 0

  def assign(self, storage_dir, intermediate_filenames, output_filename, key):
    self.storage_dir = storage_dir # ../storage
    self.intermediate_filenames = intermediate_filenames # [intermediate-1.txt, intermediate-2.txt, ...]
    self.output_filename = output_filename # output.txt
    self.key = key # apple

  def get_intermediate_filenames(self):
    return [os.path.join(self.storage_dir, self.intermediate_dir, f) for f in self.intermediate_filenames]

  def get_output_filename(self):
    return os.path.join(self.storage_dir, self.output_dir, self.output_filename)

  def execute(self):
    self.reset()
    self.reduce()
    self.emit()

  def reset(self):
    self.result = 0

  @abstractmethod
  def reduce(self):
    pass

  def emit(self):
    # Write result to file
    with open(self.get_output_filename(), 'a') as f:
      f.write(f'{self.key},{self.result}\n')
