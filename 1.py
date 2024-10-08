def count_unique_characters(input_string):
    # Используем множество (set) для хранения уникальных символов
    unique_characters = set(input_string)
    
    # Возвращаем количество уникальных символов
    return len(unique_characters)

# Пример использования
user_input = input("Введите строку: ")
unique_count = count_unique_characters(user_input)

print(f"Количество уникальных символов: {unique_count}")