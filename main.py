from stats import word_count, char_count, sort_by_count_decreasing

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    number_of_words = word_count(book_content)
    number_of_chars = char_count(book_content)
    list_of_pairs = sort_by_count_decreasing(number_of_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f" Found {number_of_words} total words")
    print("--------- Character Count -------")
     
    for dict_pair in list_of_pairs:
        if dict_pair["name"].isalpha():
            print(f"{dict_pair["name"]}: {dict_pair["num"]}")
    print("============= END ===============")

main()