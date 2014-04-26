entropy-calculation
===================


## entropycalc.py 
Provides library functions for calculating the entropy of a 
file.

It can be run by itself ```python entropycalc.py filename``` will generate a PDF 
with a histogram of the data in a file. It will print to the terminal the
entropy of that particular file as well.

# Function definitions

```calc_entropy``` - Calculates the entropy of an array that is pased in.

```entropy_of_file``` - Calculates the entropy of an entire file.

```entropy_of_file_chunks``` - Calculates the entropy of an entire file, 
splitting it into chunks of a specified size. Appends to a specified output
file. 

## scrapedir.py
Provides library functions for calculating the entropy of files within a
specified directory.

It can be run by itself in two ways. 

```python scrapedir.py input_dir output_file``` will append to an output_file, 
and calculate the entropy of all files within the input_dir. 

```python scrapedir.py input_dir output_file size_of_chunk``` will append to an
output_file, and calculate the entropy of size_of_chunk byte-wide chunks of the 
files within the input_dir.

# Function definitions

```scrapeDirectory``` - Scrapes a specified directory, appends to an output 
file, and takes in a particular chunksize.

```scrapeDirectoryTotals``` - Scrapes a specified directory, appends to an
output file, over the entire files, not just a specified chunksize.


## plot.py
This is from  [Srikanth Sundaresan](https://github.com/ssundaresan/py_utils/blob/master/plot.py). Many thanks Srikanth!
