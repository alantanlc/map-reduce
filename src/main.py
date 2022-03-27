from mapreduce.wordcount.WordCountMapWorker import WordCountMapWorker
from mapreduce.wordcount.WordCountReduceWorker import WordCountReduceWorker
import os

if __name__ == '__main__':
  storage_dir = '../storage'
  input_filenames = ['input-1.txt', 'input-2.txt', 'input-3.txt', 'input-4.txt', 'input-5.txt']
  intermediate_filenames = ['intermediate-1.txt','intermediate-2.txt','intermediate-3.txt','intermediate-4.txt','intermediate-5.txt']
  keys = ['apple', 'banana', 'cranberry', 'elderberry', 'fig']
  map_workers = []
  reduce_workers = []

  for i, j in zip(input_filenames, intermediate_filenames):
    m = WordCountMapWorker()
    m.assign(storage_dir, i, j)
    m.execute()

  with open(os.path.join(storage_dir, 'output', 'output.txt'), 'w') as f:
    pass

  for key in keys:
    r = WordCountReduceWorker()
    r.assign(storage_dir, intermediate_filenames, 'output.txt', key)
    r.execute()