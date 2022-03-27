from ..AbstractMapWorker import AbstractMapWorker
import pdb

class WordCountMapWorker(AbstractMapWorker):

  def map(self):
    # Read from input file and update word_count_map
    with open(self.get_input_filename(), 'r') as f:
      words = ' '.join(f.readlines())
      for word in words.split(' '):
        if word in self.result:
          self.result[word] += 1
        else:
          self.result[word] = 1
