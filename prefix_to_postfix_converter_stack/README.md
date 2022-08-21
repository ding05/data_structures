# A Prefix to Postfix Converter (Stack)

This program uses a traditional stack to convert prefix expressions directly to postfix expressions.

## Programming Language

Python 3.7.5

## IDE

PyCharm 2022.1.2

## Running converter

1. Make sure Python has been installed on your computer.
2. Navigate to [this](.) directory, which contains the README.md file.
3. Run the program as a module: `python -m converter -h`. This will print the help message.
4. Run the program as a module with real inputs: `python -m converter <input_filepath> <output_filepath>`
   For input, i.e. `python -m converter resources/input.txt resources/output.txt`
   For extra input, i.e. `python -m converter resources/extra_input.txt resources/extra_output.txt`

### converter Usage:

```commandline
usage: python -m converter [-h] input_filepath output_filepath

positional arguments:
  input_filepath     Input File Pathname
  output_filepath    Output File Pathname

optional arguments:
  -h, --help  show this help message and exit
```
