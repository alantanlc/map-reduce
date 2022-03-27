import AbstractMapWorker
import os

class WordCountMapWorker(AbstractMapWorker):

  def __init__(self, storage_dir):
    self.word_count = {}
    super().__init__(storage_dir) # ../storage

  def map(self):
    # Read from input file and create word_count_map
    self.word_count = {}
    with open(os.path.join(self.storage_dir, 'input', self.input_filename), 'r') as f:
      for line in f:
        for word in line:
          if word in word_count:
            self.word_count[word] += 1
          else:
            self.word_count[word] = 1

  def emit(self):
    # Write word_count_map to intermediate file
    with open(os.path.join(self.storage_dir, 'intermediate', self.intermediate_filename), 'w') as f:
      for k, v in self.word_count.items():
        f.write(f'{k},{v}')

