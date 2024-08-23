import requests
from bs4 import BeautifulSoup
import os
PATH = os.getcwd()
DATA_PATH = os.path.join(PATH, "data")
DICTIONARY_PATH = os.path.join(DATA_PATH, "dictionary.txt")
NAME_OUTPUT_MODE_2 = "examples"
NAME_OUTPUT_MODE_1 = "dictionary_with_examples"

def create_dictionary(words=None,name="dictionary", path=DATA_PATH):
    """
    Creates a simple dictionary and saves it to a text file.
    Parameters:
        words (list): A list of words to include in the dictionary. If not provided, a default list of words will be used.
        name (str): The name of the file to save the dictionary to.
        path (str): The path to the directory where the file will be saved.
    Returns:
        None
    """
    if not words: 
      words = [
          "play",
          "cinema",
          "friend",
          "word",
          "work",
          "hehe",
          "haha",
          "abcxyz",
          "abc"
      ]

    # Construct the full file path
    file_path = f"{path}/{name}.txt"

    # Write the words to the file
    with open(file_path, "w") as file:
        for word in words:
            file.write(f"{word}\n")
    
    print(f"File created successfully at: {file_path}")
    
def crawl_example_sentences(word,min_len=None,number_example=None):
    """
    Crawls example sentences for a given word from the Merriam-Webster dictionary website.

    Parameters:
        word (str): The word to search for.
        min_len (int): The minimum length of the example sentences to return. Defaults to None.
        number_example (int): The number of example sentences to return. Defaults to None.
    Returns:
        List of example sentences.
    """
    url = f'https://www.merriam-webster.com/dictionary/{word}'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find all <span> elements with the specific class
        spans = soup.find_all('span', class_='t has-aq')

        # Extract and return the text content ofinf each matching span
        sentences = [span.text.strip() for span in spans]
        if(min_len):
            sentences = [sentence for sentence in sentences if len(sentence.split()) >= min_len]
        if(number_example):
            sentences = sentences[:number_example]
        return sentences
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

def find_examples_for_dictionary(file_dictionary_path= DICTIONARY_PATH , min_len=None, number_example=None, name_output=NAME_OUTPUT_MODE_2, path=PATH, name_error=None):
    """
    Finds example sentences for each word in a provided dictionary file and saves them in a specified format to a new file.

    Parameters:
        file_dictionary_path (str): The path to the input dictionary file containing one word per line.
        min_len (int): The minimum length of the example sentences to return (in words).
        number_example (int): The number of example sentences to return for each word.
        name_output (str): The name of the output file to save the examples to (without extension).
        path (str): The path to the directory where the output file will be saved.
        name_error (str): The name of the file to save words for which no examples were found. If None, no error file is created.

    Returns:
        word_error (list): A list of words for which no examples were found.
    """
    # Construct the full path for the output file
    output_file_path = os.path.join(path, f"{name_output}.txt")

    # Open the dictionary file and read the words
    with open(file_dictionary_path, "r") as dictionary_file:
        words = [line.strip() for line in dictionary_file if line.strip()]
    word_error = []
    # Open the output file for writing
    with open(output_file_path, "w") as output_file:
        for word in words:
            # Find example sentences for the word
            example_sentences = crawl_example_sentences(word, min_len=min_len, number_example=number_example)
            # Write the number of examples and the examples themselves, separated by a comma
            if example_sentences:
                num_examples = len(example_sentences)
                examples_str = "| ".join(example_sentences)
                output_file.write(f"{num_examples} | {examples_str}\n")
            else:
                # If no examples are found, write 0
                output_file.write("0 | No examples found\n")
                word_error.append(word)

    print(f"Output file created successfully at: {output_file_path}")
    if len(word_error) > 0:
        if name_error:
            output_file_path_error = os.path.join(path, f"{name_error}.txt")
            with open(output_file_path_error, "w") as output_file_error:
                for word in word_error:
                    output_file_error.write(f"{word}\n")
        print(f"Cannot find examples for {len(word_error)} word/words ")
    return word_error

def save_word_with_one_example(file_dictionary_path = DICTIONARY_PATH,name_output=NAME_OUTPUT_MODE_1, path=PATH, name_error=None):
    """
    Saves words from a dictionary file along with one example sentence for each word to an output file.

    Parameters:
        file_dictionary_path (str): The path to the input dictionary file containing one word per line.
        name_output (str): The name of the output file to save the words and their examples to (without extension).
        path (str): The directory where the output file will be saved.
        name_error (str): The name of the file to save words for which no examples were found. If None, no error file is created.
    
    Returns:
        list: A list of words for which no examples were found.
    """
    # Construct the full path for the output file
    file_path = os.path.join(path, f"{name_output}.txt")

    word_error = []
    # Open the dictionary file and read the words
    with open(file_dictionary_path, "r") as dictionary_file:
        words = [line.strip() for line in dictionary_file if line.strip()]
        
    # Open the output file for writing
    with open(file_path, "w") as output_file:
        for word in words:
            example_sentences = crawl_example_sentences(word, number_example=1)
            if example_sentences:
              example = example_sentences[0] 
            else:
                # If no examples are found, write 0
                example = "No examples found"
                word_error.append(word)
            # Write the number of examples and the examples themselves, separated by a comma
            output_file.write(f"{word} | {example}\n")

    print(f"Output file created successfully at: {file_path}")
    if len(word_error) > 0:
        if name_error:
            output_file_path_error = os.path.join(path, f"{name_error}.txt")
            with open(output_file_path_error, "w") as output_file_error:
                for word in word_error:
                    output_file_error.write(f"{word}\n")
        print(f"Cannot find examples for {len(word_error)} word/words ")
    return word_error
