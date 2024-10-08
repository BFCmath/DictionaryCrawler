# DictionaryCrawler

**DictionaryCrawler** is a Python-based tool designed to crawl example sentences for words from the *online* dictionary like *Cambridge*, *Oxford*, ... using *BeautifulSoup*. This utility allows you to easily obtain example sentences for a list of words provided in a text file.

**Special thanks to Nam Anh for the insightful ideas**

## Installation
1. Clone the Reposity
```bash
git clone https://github.com/BFCmath/DictionaryCrawler.git
cd DictionaryCrawler
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Prepare the Words-dictionary File
+ Replace your dictionary file, named `dictionary.txt`, in the data folder.
+ Ensure that each line of the file contains a single word.

2. Running the script
Choose one of the following modes based on your needs:
+ Generate a Text File with One Example per Word
```bash
python main.py 1
```
+ Generate a Text File with Multiple Examples
```bash 
python main.py 2
```
For detailed information about available arguments and configuration options, refer to [here](src/README.md).

## DEMO 
You can try a demo of this tool without cloning the repository by following this [Colab link](https://colab.research.google.com/drive/1JSLPjd-864mfUQPoGnWbNbQ_5AQw-1jK?usp=sharing).