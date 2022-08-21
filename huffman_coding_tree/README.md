# A Huffman Coding Tree

This program performs Huffman encoding and decoding with a binary tree.

## Programming Language

Python 3.7.5

## IDE

PyCharm 2022.1.2

## Running converter

1. Make sure Python has been installed on your computer.
2. Navigate to [this](.) directory, which contains the README.md file.
3. Run the program as a module: `python -m converter -h`. This will print the help message.
4. Run the program as a module with real inputs: `python -m converter <input_freq_filepath> <input_expression_filepath> <output_filepath> <message_filepath>`
   For the input for encoding, i.e. `python -m converter resources/FreqTable.txt resources/ClearText.txt resources/ClearText_Output.txt resources/ClearText_Message.txt`
   For the input for decoding, i.e. `python -m converter resources/FreqTable.txt resources/Encoded.txt resources/Encoded_Output.txt resources/Encoded_Message.txt`

### converter Usage:

```commandline
usage: python -m converter [-h] input_freq_filepath input_expression_filepath output_filepath message_filepath

positional arguments:
  input_freq_filepath        Input Frequency Table Pathname
  input_expression_filepath  Input Expression File Pathname
  output_filepath            Output File Pathname
  message_filepath           Message File Pathname

optional arguments:
  -h, --help  show this help message and exit
```
