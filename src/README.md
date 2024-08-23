# Usage
This `README` provides an overview of your project, explains its features, shows how to use the main functions, and includes important notes about configuration and usage. 

You may want to adjust or expand certain sections based on your specific project needs or any additional functionality you plan to add.

## Configuration
The project uses several predefined paths:

+ `PATH`: Current working directory
+ `DATA_PATH`: Directory for data files (default: `PATH/data`)
+ `DICTIONARY_PATH`: Path to the default dictionary file (default: `DATA_PATH/dictionary.txt`)
+ `NAME_OUTPUT_MODE_2`: Default output name for multiple examples mode (default: `"examples"`)
+ `NAME_OUTPUT_MODE_1`: Default output name for single example mode (default: `"dictionary_with_examples"`)

You can modify these in the `utils.py` file if needed.

## Arguments

- `MODE`: Required. Choose '1' to find one example for each word, or '2' to find multiple examples for each word.

### Options

- `--name_output`: Name of the output file (without extension). If not provided, defaults to **"dictionary_with_examples"** for mode 1 or **"examples"** for mode 2.
- `--name_error`: Name of the error file (without extension) to store words for which no examples were found.
- `--file_dictionary_path`: Path to the input dictionary file. If not provided, uses the default DICTIONARY_PATH.
- `--min_len`: (Mode 2 only) Minimum length of example sentences to return.
- `--number_example`: (Mode 2 only) Number of example sentences to return for each word.


## Functions
+ `create_dictionary`: Creates a simple dictionary and saves it to a text file.
+ `crawl_example_sentences`: Crawls example sentences for a given word from the Merriam-Webster dictionary website.
+ `find_examples_for_dictionary`: Finds example sentences for each word in a provided dictionary file and saves them to a new file.
+ `save_word_with_one_example`: Saves words from a dictionary file along with one example sentence for each word to an output file.



## Demo
You can try a demo of this tool without cloning the repository by following this [Colab link](https://colab.research.google.com/drive/1JSLPjd-864mfUQPoGnWbNbQ_5AQw-1jK?usp=sharing).