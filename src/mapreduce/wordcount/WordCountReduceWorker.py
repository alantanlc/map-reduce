from ..AbstractReduceWorker import AbstractReduceWorker

class WordCountReduceWorker(AbstractReduceWorker):

  def reduce(self):
    # Read from intermedate files and collect results
    for filename in self.get_intermediate_filenames():
      with open(filename, 'r') as f: # apple,3\nbanana,1
        for line in f:
          word, count = line.strip().split(',') # word = 'apple', count = 3
          if word == self.key:
            self.result += int(count)
