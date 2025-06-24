def count_words(book_text: str) -> int:
    return len(book_text.split())

def number_of_characters(book_text: str) -> dict:
    book_text = book_text.lower()
    char_count = {}

    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_dic(book_dic: dict) -> dict:
    return dict(sorted(book_dic.items(), key=lambda item: item[1], reverse=True))