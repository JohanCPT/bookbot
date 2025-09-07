from stats import word_count, char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_content = get_book_text("books/frankenstein.txt")
    #print(book_content)
    number_of_words = word_count(book_content)
    number_of_chars = char_count(book_content)
    print(f"{number_of_words} words found in the document")
    print(number_of_chars)
    
main()
