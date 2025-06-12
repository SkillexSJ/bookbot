import sys
from bookbot.stats import count_word
from bookbot.stats import count_char  
from bookbot.stats import sort_it

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = count_word(book_text)
    char_count = count_char(book_text)
    sort_kori = sort_it(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sort_kori:
        char = entry["char"]
        count = entry["num"]
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
