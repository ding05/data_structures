# Quick and Merge Sorts

This program performs a QuickSort and a Merge Sort on integer arrays and compare their performance.

## Programming Language

Python 3.7.5

## IDE

PyCharm 2022.1.2

## Running sorts

1. Make sure Python has been installed on your computer.
2. Navigate to [this](.) directory, which contains the README.md file.
3. Run the program as a module: `python -m sorts -h`. This will print the help message.
4. Run the program as a module with real inputs: `python -m sorts <input_dirpath> <output_dirpath> <message_filepath>`
   I.e. `python -m sorts resources/input resources/output resources/Message.txt`

### sorts Usage:

```commandline
usage: python -m sorts [-h] input_dirpath output_dirpath message_filepath

positional arguments:
  input_dirpath              Input Directory Pathname
  output_dirpath             Output Directory Pathname
  message_filepath           Message File Pathname

optional arguments:
  -h, --help  show this help message and exit
```