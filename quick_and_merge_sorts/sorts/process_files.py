from sorts.input import *
from sorts.output import *
from sorts.quick_sort import *
from sorts.merge_sort import *
# This package is required for recording the processing time.
from datetime import datetime

def process_files(input_dirpath: str, output_dirpath: str,
                  message_filepath: str) -> None:
  """
  Read the DAT files with unsorted integers in the given directory and
  perform four types of QuickSorts (with two including an Insertion Sort),
  record the performance, and output the sorted integers and the required
  messages.
  :param input_dirpath: the path to the directory that contains input DAT
  files
  :param output_dirpath: the path to the directory that contains output DAT
  files
  :param message_filepath: the path to the output TXT file
  """
  # Get the filenames in the input directory.
  filenames = get_filenames(input_dirpath)

  # Messages of the sorts' performance
  # Each item is a line in the TXT file, so it starts with the attribute line.
  perform_list = ["Filename QSA_C QSA_T QSB_C QSB_T QSC_C QSC_T QSD_C QSD_T" +
                  " NMS_C NMS_T"]

  # Run the sorts and record the performance one file by one file.
  for filename in filenames:
    print("Read " + filename + ".")
    input_filepath = str(input_dirpath) + "/" + filename

    # Read the unsorted integer list from the DAT file.
    unsorted_integer_list = input(input_filepath)

    # Name of the sort's performance without ".dat"
    perform = filename[:-4] + " "

    # Perform Type A of the Quicksort.
    # Record the time
    start = datetime.now()
    sorted_integer_list, num_compare = quick_sort(unsorted_integer_list, "A")
    stop = datetime.now()

    # Output the DAT file.
    # Rename the filename by adding the name of the sorting algorithm.
    output_filename = filename[:-4] + "_QSA.dat"
    output_filepath = str(output_dirpath) + "/" + output_filename
    output(sorted_integer_list, output_filepath)

    # Record the processing time and convert it into a string.
    time_diff = stop - start
    perform += str(num_compare) + " " + str(time_diff)[5:] + " "

    # Print a completion message.
    print("Finish " + output_filename + ".")

    # Repeat the steps above for the other four sorts. Comments are ommited.
    # Perform Type B of the Quicksort.
    start = datetime.now()
    sorted_integer_list, num_compare = quick_sort(unsorted_integer_list, "B")
    stop = datetime.now()
    output_filename = filename[:-4] + "_QSB.dat"
    output_filepath = str(output_dirpath) + "/" + output_filename
    output(sorted_integer_list, output_filepath)
    time_diff = stop - start
    perform += str(num_compare) + " " + str(time_diff)[5:] + " "
    print("Finish " + output_filename + ".")

    # Perform Type C of the Quicksort.
    start = datetime.now()
    sorted_integer_list, num_compare = quick_sort(unsorted_integer_list, "C")
    stop = datetime.now()
    output_filename = filename[:-4] + "_QSC.dat"
    output_filepath = str(output_dirpath) + "/" + output_filename
    output(sorted_integer_list, output_filepath)
    time_diff = stop - start
    perform += str(num_compare) + " " + str(time_diff)[5:] + " "
    print("Finish " + output_filename + ".")

    # Perform Type D of the Quicksort.
    start = datetime.now()
    sorted_integer_list, num_compare = quick_sort(unsorted_integer_list, "D")
    stop = datetime.now()
    output_filename = filename[:-4] + "_QSD.dat"
    output_filepath = str(output_dirpath) + "/" + output_filename
    output(sorted_integer_list, output_filepath)
    time_diff = stop - start
    perform += str(num_compare) + " " + str(time_diff)[5:] + " "
    print("Finish " + output_filename + ".")

    # Perform the Natural Merge Sort.
    start = datetime.now()
    sorted_integer_list, num_compare = natural_merge_sort(unsorted_integer_list)
    stop = datetime.now()
    output_filename = filename[:-4] + "_NMS.dat"
    output_filepath = str(output_dirpath) + "/" + output_filename
    output(sorted_integer_list, output_filepath)
    time_diff = stop - start
    perform += str(num_compare) + " " + str(time_diff)[5:] + " "
    print("Finish " + output_filename + ".")

    # Append the message,which contains the filename and the processing time
    # of the five sorts, to the message list.
    perform_list.append(perform)

  # Write the performance message list into a TXT file.
  message(perform_list, message_filepath)