import sys
from stats import get_num_words
from stats import get_tcotal_charaters
from stats import sorted_dic_to_list
from stats import sort_on

def main():
    if len(sys.argv) == 2:

        with open(sys.argv[1]) as f:
            file_contents = f.read()
            totalWords = get_num_words(file_contents.split())
            print(f"Found {totalWords} total words")
            print(f"{get_tcotal_charaters(file_contents)}")
            print(f"{sorted_dic_to_list(get_tcotal_charaters(file_contents))}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()