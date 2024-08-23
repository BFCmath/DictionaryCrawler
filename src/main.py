import argparse
from utils import find_examples_for_dictionary, save_word_with_one_example, DICTIONARY_PATH, NAME_OUTPUT_MODE_1, NAME_OUTPUT_MODE_2

def main(args):
    # Common parameters
    file_dictionary_path = args.file_dictionary_path or DICTIONARY_PATH
    name_output = args.name_output or (NAME_OUTPUT_MODE_1 if args.MODE == '1' else NAME_OUTPUT_MODE_2)
    name_error = args.name_error 

    if args.MODE == '1':
        save_word_with_one_example(
            file_dictionary_path=file_dictionary_path,
            name_output=name_output,
            name_error=name_error
        )
    elif args.MODE == '2':
        find_examples_for_dictionary(
            file_dictionary_path=file_dictionary_path,
            name_output=name_output,
            name_error=name_error,
            min_len=args.min_len,
            number_example=args.number_example
        )
    else:
        print("Invalid mode. Use 1 or 2.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl word examples from online dictionary websites.")
    
    # Add arguments
    parser.add_argument('MODE', choices=['1', '2'],
                        help="""Mode of operation: (1) find one example for each word or (2) find many examples for each word""")
    parser.add_argument('--name_output', type=str, help="Name of the output file (without extension)")
    parser.add_argument('--name_error', type=str, help="Name of the error file (without extension)")
    parser.add_argument('--file_dictionary_path', type=str, help="Path to the dictionary file")
    parser.add_argument('--min_len', type=int, help="Minimum length of example sentences (only for mode 2)")
    parser.add_argument('--number_example', type=int, help="Number of example sentences to return (only for mode 2)")

    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args)