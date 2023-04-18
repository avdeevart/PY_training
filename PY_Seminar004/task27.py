# Задача №27: Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells

text = input("Введите текст: ")  # Запросить ввод текста с консоли

# Разделить текст на слова, привести слова к нижнему регистру и подсчитать уникальные слова
unique_words = set(word.lower() for word in text.split())

# Вывести количество уникальных слов
print("Количество уникальных слов в тексте:", len(unique_words))