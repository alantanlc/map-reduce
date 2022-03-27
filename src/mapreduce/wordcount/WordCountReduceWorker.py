from ..AbstractReduceWorker import AbstractReduceWorker
import pdb

class WordCountReduceWorker(AbstractReduceWorker):

  def reduce(self):
    # Read from intermedate files and collect results
    for filename in self.get_intermediate_filenames():
      with open(filename, 'r') as f: # a,1\nb,1
        for line in f:
          word, count = line.strip().split(',') # word = 'a', count = 1
          if word == self.key:
            self.result += int(count)
