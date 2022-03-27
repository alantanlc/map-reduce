import os

class Master:

  def __init__(self, map_workers, reduce_workers, storage_dir, input_files, intermediate_files, output_file, keys):
    self.map_workers = map_workers
    self.reduce_workers = reduce_workers
    self.storage_dir = storage_dir
    self.output_dir = 'output'
    self.input_files = input_files
    self.intermediate_files = intermediate_files
    self.output_file = output_file
    self.keys = keys

  def assign_map_workers(self):
    # For now let's assume that num of workers and input_files are the same
    for worker, input_file, intermediate_file in zip(self.map_workers, self.input_files, self.intermediate_files):
      worker.assign(self.storage_dir, input_file, intermediate_file)

  def assign_reduce_workers(self):
    # Assign each reduce worker with a key
    # All reduce workers will write to the same output file
    for worker, key in zip(self.reduce_workers, self.keys):
      worker.assign(self.storage_dir, self.intermediate_files, self.output_file, key)

  def clear_output(self):
    with open(os.path.join(self.storage_dir, 'output', self.output_file), 'w') as f:
      pass

  def run(self):
    # Clear output file
    self.clear_output()

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
