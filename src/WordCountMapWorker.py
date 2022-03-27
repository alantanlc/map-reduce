import AbstractMapWorker

class WordCountMapWorker(AbstractMapWorker):

  def map(self):
    # Read from input file and update word_count_map
    with open(self.get_input_filename(), 'r') as f:
      for line in f:
        for word in line:
          if word in result:
            self.result[word] += 1
          else:
            self.result[word] = 1

if __name__ == '__main__':
  pass
