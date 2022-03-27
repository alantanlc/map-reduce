import AbstractReduceWorker
import os

class WordCountReduceWorker(AbstractReduceWorker):

  def __init__(self, key, intermediate_filename, output_filename):
    super().__init__(key, intermedidate_filename, output_filename)

  def reduce(self):
    # Read from intermedate files and collect results
    self.result = 0
    for filename in self.intermediate_filenames:
      with open(filename, 'r') as f: # a,1\nb,1
        for line in f:
          word, count = line.split(',') # word = 'a', count = 1
          if word == self.key:
            self.result += 1
