from mapreduce.wordcount.WordCountMapWorker import WordCountMapWorker
from mapreduce.wordcount.WordCountReduceWorker import WordCountReduceWorker
from mapreduce.Master import Master

if __name__ == '__main__':
  # Init parameters
  storage_dir = '../storage'
  output_dir = '../output'
  input_filenames = ['input-1.txt', 'input-2.txt', 'input-3.txt', 'input-4.txt', 'input-5.txt']
  intermediate_filenames = ['intermediate-1.txt','intermediate-2.txt','intermediate-3.txt','intermediate-4.txt','intermediate-5.txt']
  output_filename = 'output.txt'
  keys = ['apple', 'banana', 'cranberry', 'durian', 'elderberry', 'fig']
  map_workers = [WordCountMapWorker() for i in range(len(input_filenames))]
  reduce_workers = [WordCountReduceWorker() for i in range(len(keys))]

  # Master worker
  master = Master(map_workers, reduce_workers, storage_dir, input_filenames, intermediate_filenames, output_filename, keys)
  master.assign_map_workers()
  master.assign_reduce_workers()
  master.run()