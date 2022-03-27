class Master:

  def __init__(self, map_workers, reduce_workers, input_files, output_file):
    self.map_workers = workers
    self.reduce_workers = worker
    self.input_files = input_files
    self.output_file = output_file
    self.assign_map(self.map_workers, self.input_files)
    self.assign_reduce(self.reduce_workers, self.output_file)

  def assign_map(self, workers, input_files):
    # For now let's assume that num of workers and input_files are the same
    for worker, file_name in zip(workers, input_files):
      worker.assign(file_name)

  def assign_reduce(self, workers, output_file):
    # All reduce workers will write to the same output file
    for worker in workers:
      worker.assign(output_file)

  def run(self):
    # Map
    for worker in self.map_workers:
      worker.execute()

    # Wait for all map workers to complete execution
    # ...

    # Reduce
    for worker in self.reduce_workers:
      worker.execute()

    # Wait for all reduce workers to complet execution
    # ...

    # Get results from output.txt
    # ...
