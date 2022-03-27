from abc import ABC, abstractmethod

def AbstractReduceWorker(AbstractWorker):

  def __init__(self):
    self.intermediate_filenames = None
    self.output_filename = None

  def assign(self, intermediate_filenames, output_filename):
    self.intermediate_filenames = intermediate_filenames # [intermediate-1.txt, intermediate-2.txt, ...]
    self.output_filename = output_filename # output.txt

  def execute(self):
    self.reduce()
    self.emit()

  @abstractmethod
  def reduce(self):
    pass

  @abstractmethod
  def emit(self):
    pass
