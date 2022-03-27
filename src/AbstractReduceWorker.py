from abc import ABC, abstractmethod
import AbstractWorker
import os

def AbstractReduceWorker(AbstractWorker):

  def __init__(self):
    self.intermediate_dir = 'intermediate'
    self.output_dir = 'output'
    self.intermediate_filenames = None
    self.output_filename = None
    self.key = None
    self.result = None

  def assign(self, storage_dir, intermediate_filenames, output_filename, key):
    self.storage_dir = storage_dir # ../storage
    self.intermediate_filenames = intermediate_filenames # [intermediate-1.txt, intermediate-2.txt, ...]
    self.output_filename = output_filename # output.txt
    self.key = key # a

  def get_intermediate_filenames(self):
    return [os.path.join(self.storage_dir, self.intermediate_dir, f) for f in self.intermediate_filenames()]

  def get_output_filename(self):
    return os.path.join(self.storage_dir, self.output_dir, self.output_filename)

  def execute(self):
    self.reset_result()
    self.reduce()
    self.emit()

  def reset_result():
    self.result = None

  @abstractmethod
  def reduce(self):
    pass

  def emit(self):
    # Write result to file
    with open(self.get_output_filename(), 'w') as f:
      f.write(f'{self.key},{self.result}')
