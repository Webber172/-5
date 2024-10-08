def find_duplicate_words(input_string):
    words = input_string.lower().split()

    word_count = {}
    
    for word in words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    duplicates = [word for word, count in word_count.items() if count > 1]
    
    return duplicates

user_input = ("введите текст")
duplicates = find_duplicate_words(user_input)

if duplicates:
    print(f"Дублирующиеся слова: {', '.join(duplicates)}")
else:
    print("Нет дублирующихся слов.")