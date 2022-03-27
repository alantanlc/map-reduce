# Map Reduce

## Components

### User Program

Tasks:
1. Fork master and workers

###  Master

Variables:
1. List of workers
1. List of files

Functions:
1. constructor
  1. initializes workers list
  1. initializes files list
1. assignMap function
  1. e.g. each MapWorker takes an input file
1. assignReduce function
  1. e.g. each ReduceWorker takes an intermediate file
1. run function
  1. for each worker, execute

### AbstractWorker

Functions:
1. abstract execute function
1. abstract read function (read)
1. abstract emit function (write)

### AbstractMapWorker

Variables:
1. input_filename
1. intermediate_filename

Functions:
1. implements execute function which calls abstract map function
1. abstract map function

#### WordCountMapWorker

Functions:
1. implements map function
  1. read file
  1. split content into words
  1. generate word-count map
1. implements emit function
  1. writes results to intermediate

### AbstractReduceWorker

Variables:
1. output_filename

Functions:
1. implements execute function which calls reduce function
1. abstract reduce function

#### WordCountReduceWorker

Functions:
1 .implements reduce function
  1. read file
  1. collect results
1. implements emit function
  1. writes results to file

