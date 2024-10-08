def count_unique_words(input_string):

    words = input_string.lower().split()
    
    unique_words = set(words)
    
    return len(unique_words)

user_input = input("Введите строку: ")
unique_count = count_unique_words(user_input)

print(f"Количество уникальных слов: {unique_count}")