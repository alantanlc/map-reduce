from mapreduce.wordcount.WordCountMapWorker import WordCountMapWorker

if __name__ == '__main__':
  w = WordCountMapWorker()
  w.assign('../storage', 'input-1.txt', 'intermediate-1.txt')
  w.execute()