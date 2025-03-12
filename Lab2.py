import matplotlib.pyplot as plt
from collections import Counter
import string



my_text = 'MDU2ODMzODU1NDg3MDU2ODI1OTYyNjMxMzQ0NTEwMzkzMzA5MzQ0NTI1OTYzMzg1MTQ1NDI2NzIzNDQ1MjA3NzE2MDUyNjcyMTExODU0ODc2MjkyNjUxODE2MDUzMzg1MTExODUwNjgwNTY4MTYwNTMzMDkzNDQ1Mjg5NDY5MDU1NDg3NTA2ODM0NDUyMDc3NjI5MjYyOTIxMTE4MDU2ODE2MDUzMzg1NTQ4NzY5MDU2MjkyMjU5NjM0NDUyMzIwMTYwNTYyOTIzMTg1MzQ0NTM0ODMxNjA1NjkwNTU0ODc2OTA1MzMwOTUwNjgzNDQ1MzM4NTI1OTYwNzM4MzQ0NTA3MzgxMDM5NTQ4NzIwNzc1MDY4MzQ0NTIwNzcxNjA1MjY3MjExMTg1NDg3NjI5MjY1MTgxNjA1MzM4NTExMTg1MDY4MDU2ODE2MDUzMzA5MzQ0NTMzODUyMzIwNTQ4NzA1NjgxNjA1MzQ0NTM0ODMxNjA1NjI5MjU5MDEwNTY4MzQ0NTY5MDUyNTk2NTQ4NzYyOTIzNDQ1MzMwOTA1NjgxNDU0MDU2ODE2MDUzMzg1NTA0NzM0NDU0MDc3MzM4NTExMTgzMzg1MjU5NjA1NjgzMzA5MDU2ODM0NDUyNTk2MzM4NTE0NTQyNjcyMzQ0NTIwNzcxNjA1MjY3MjExMTg1NDg3NjI5MjM0NDUzMzA5MjY3MjMzMDk1NDg3MDU2ODMxODUzMzA5MjYzMTM0NDU1NDg3NTA2ODA1NjgzNDQ1MzQ4MzE2MDUwNTY4MzM4NTU5MDEzNDQ1NjkwNTI1OTY1NDg3NjI5MjM0NDU2MjkyMjU5NjA1NjgzNDQ1NjI5MjIzMjAzNDQ1NTQ4NzUwNjgwNTY4MzE4NTMyOTUzNDQ1NDA3NzI1OTYxOTUxMzI5NTM0NDUyMzIwMzM4NTMxODU2MjkyMTAzOTMzMDk1MDQ3MjY3MjM0NDU1MDQ3MDU2ODA3MzgzNDQ1NTQ4NzYyOTIzNDQ1NTQ4NzUwNjgwNTY4MzQ0NTEwMzkzMzA5MzQ0NTE0NTQ2OTA1MjA3NzU0ODc2MjkyMTYwNTI2NzIzNDQ1NjkwNTI1OTYzNDQ1NTQ4NzUwNjgwNTY4MzQ0NTM0ODMzMzg1NTQ4NzU0ODc1MDQ3MDU2ODM0NDU2MjkyMjMyMDM0NDUzMTg1NjkwNTA3MzgyODk0MzM4NTI2NzI2NjI4MzQ0NTMzODUyNTk2MDczODM0NDU1NDg3NjI5MjM0NDUzNDQ1NTQ4NzUwNjgwNTY4MzQ0NTExMTgxMDM5MzQ4MzUwNDc2OTA1MjA3NzMzODU1NDg3NjkwNTYyOTIyNTk2MzQ0NTYyOTIyMzIwMzQ0NTU0ODc1MDY4MzM4NTU0ODczNDQ1MjMyMDMzODUyMDc3NTQ4NzM0NDU2OTA1MjU5NjM0NDU1NDg3NTA2ODA1NjgzNDQ1MjA3NzUwNjg2OTA1MjA3NzMzODU2NTE4NjI5MjM0NDU1NDg3MTYwNTY5MDUzNDgzMTAzOTI1OTYwNTY4MzQ0NTMzMDk1MDY4NjI5MjE2MDU1NDg3NTA0NzI2NzIzNDQ1MzM4NTIzMjA1NDg3MDU2ODE2MDUzNDQ1NTQ4NzUwNjgwNTY4MzQ0NTM0ODMzMzg1NTQ4NzU0ODc1MDQ3MDU2ODMyOTUzNDQ1NTQ4NzUwNjg2MjkyMTAzOTY1MTg1MDY4MzQ0NTU0ODc1MDY4MDU2ODM0NDU0MDc3MzM4NTExMTgzMzg1MjU5NjA1NjgzMzA5MDU2ODM0NDUzMzA5MDU2ODA1NjgzMTg1MzQ0NTI1OTY2MjkyNTQ4NzM0NDU1NDg3NjI5MjM0NDU1MDY4MzM4NTE0NTQwNTY4MzQ0NTI1OTY2MjkyNTQ4NzY5MDUyMDc3MDU2ODA3MzgzNDQ1MjMyMDYyOTIxNjA1MzQ0NTU0ODc1MDY4MDU2ODI2NzIzNDQ1NTkwMTA1NjgxMTE4NTQ4NzM0NDUxMDM5MzMwOTY5MDUyNTk2NjUxODM0NDU1NDg3NTA2ODA1NjgzNDQ1NDA3NzI1OTYxOTUxMzQ0NTMzMDkyNjcyMzMwOTU0ODcwNTY4MzE4NTI2MzEzNDQ1MzM4NTM0NDUxMDM5MzMwOTMzODU1NDg3MzQ0NTU0ODc1MDY4MDU2ODM0NDUwNTY4MjU5NjA3MzgzNDQ1NjI5MjIzMjAzNDQ1NTQ4NzUwNjgwNTY4MzQ0NTI4OTQzMzg1MTYwNTMyOTUzNDQ1NjI5MjI1OTYzNDQ1MzM4NTExMTgxNjA1NjkwNTUwNDczMjk1MzQ0NTM0ODMxNjA1NjkwNTU0ODczMzg1NjkwNTI1OTYzMjcyMzMwOTM0NDU1NDg3NjI5MjExMTgzNDQ1MzE4NTY5MDU1MDQ3NjkwNTU0ODczMzg1MTYwNTI2NzIzNDQ1NjI5MjIzMjAyMzIwNjkwNTIwNzcwNTY4MTYwNTMzMDkzNDQ1Mjg5NDA1NjgxNjA1MDU2ODM0NDU1NDg3NjI5MjUwNDcwNzM4MzQ0NTU0ODc1MDY4MzM4NTU0ODczNDQ1NTQ4NzUwNjgwNTY4MjY3MjM0NDUyMDc3NjI5MjEwMzk1MDQ3MDczODM0NDUyNTk2MDU2ODE0NTQwNTY4MTYwNTM0NDUxNjA1MDU2ODE0NTQwNTY4MzM4NTUwNDczNDQ1NTQ4NzUwNjgzMzg1NTQ4NzM0NDU1NDg3NTA2ODA1NjgzNDQ1NjUxODA1NjgxNjA1MzE4NTMzODUyNTk2MzQ0NTA1NjgyNTk2NjkwNTY1MTgzMTg1MzM4NTM0NDUyMDc3NjkwNTExMTg1MDY4MDU2ODE2MDUzNDQ1NTA2ODMzODUwNzM4MzQ0NTM0ODMwNTY4MDU2ODI1OTYzNDQ1MzQ4MzE2MDU2MjkyNTkwMTA1NjgyNTk2MzQ0NTM0ODMwNTY4MjA3NzMzODUxMDM5MzMwOTA1NjgzNDQ1NjkwNTU0ODczNDQ1Mjg5NDYyOTIxMDM5NTA0NzA3MzgzNDQ1NjUxODY5MDUxNDU0MDU2ODM0NDU1NDg3NTA2ODA1NjgzNDQ1MDczODA1NjgyMzIwMDU2ODMzODU1NDg3MDU2ODA3MzgzNDQ1MDU2ODI1OTYwNTY4MzE4NTI2NzIzNDQ1NTQ4NzUwNjgwNTY4MzQ0NTIwNzc1MDY4MzM4NTI1OTYyMDc3MDU2ODM0NDU1NDg3NjI5MjM0NDUzMzA5MzM4NTI2NzIzNDQ1NTQ4NzUwNjgwNTY4MjY3MjM0NDUyODk0MDU2ODE2MDUwNTY4MzQ0NTI1OTY2MjkyNTQ4NzM0NDUyODk0MDU2ODUwNDc1MDQ3MzQ0NTMzODUyNTk2MDczODM0NDUyMzIwMzM4NTY5MDUxNjA1NTA0NzI2NzIzNDQ1MzQ4Mw=='
# Функція для визначення використаного алфавіту
def get_alphabet(text):
    return sorted(set(text))


# Функція для підрахунку частоти символів
def get_char_frequencies(text):
    return Counter(text)


# Функція для підрахунку біграм
def get_bigrams(text):
    bigrams = [text[i:i + 2] for i in range(len(text) - 1)]
    return Counter(bigrams)


# Функція для підрахунку трірам
def get_trigrams(text):
    trigrams = [text[i:i + 3] for i in range(len(text) - 2)]
    return Counter(trigrams)


# Функція для побудови гістограми
def plot_histogram(freqs, title):
    chars, counts = zip(*freqs)
    plt.figure(figsize=(12, 6))
    plt.bar(chars, counts, color='yellow')
    plt.title(title)
    plt.xlabel('Символи')
    plt.ylabel('Частота')
    plt.show()


# Основна функція для аналізу тексту
def analyze_text(text):
    # Фільтрація тексту для використання тільки допустимих символів
    allowed_chars = string.ascii_letters + string.digits + string.punctuation + " "
    filtered_text = ''.join([char for char in text if char in allowed_chars]).replace(' ','_')

    # Отримуємо алфавіт
    alphabet = get_alphabet(filtered_text)
    print(f"Використаний алфавіт: {''.join(alphabet)}")

    # Отримуємо частоту повторень символів
    frequencies = get_char_frequencies(filtered_text)

    # Виводимо частоти символів за алфавітним порядком
    print("\nЧастоти символів (за алфавітним порядком):")
    for char in sorted(frequencies):
        print(f"{char}: {frequencies[char]}")

    # Виводимо частоти символів за спаданням частоти
    sorted_by_frequency = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    print("\nЧастоти символів (за спаданням частоти):")
    for char, freq in sorted_by_frequency:
        print(f"{char}: {freq}")

    # Побудова гістограм
    plot_histogram(sorted(frequencies.items()), "Частоти символів (за алфавітним порядком)")
    plot_histogram(sorted_by_frequency, "Частоти символів (за спаданням частоти)")

    # Аналіз біграм
    bigram_frequencies = get_bigrams(filtered_text)
    filtered_bigrams = [(k, v) for k, v in bigram_frequencies.items()][:15]
    sorted_bigrams = sorted(filtered_bigrams, key=lambda x: x[1], reverse=True)

    print("\nБіграми:")
    for bigram, freq in sorted_bigrams:
        print(f"{bigram}: {freq}")

    # Побудова гістограми для біграм
    if sorted_bigrams:
        plot_histogram(sorted_bigrams, "Частоти біграм")

    # Аналіз трірам
    trigram_frequencies = get_trigrams(filtered_text)
    filtered_trigrams = [(k, v) for k, v in trigram_frequencies.items()][:15]
    sorted_trigrams = sorted(filtered_trigrams, key=lambda x: x[1], reverse=True)

    print("\nТріграми:")
    for trigram, freq in sorted_trigrams:
        print(f"{trigram}: {freq}")

    # Побудова гістограми для трірам
    if sorted_trigrams:
        plot_histogram(sorted_trigrams, "Частоти тріграм ")

    # Пошук повторень символів для 2, 3 і 4 символів
    for n in [2, 3, 4]:
        sequences = [filtered_text[i:i + n] for i in range(len(filtered_text) - n + 1)]
        sequence_frequencies = Counter(sequences)
        sorted_sequences = sorted(sequence_frequencies.items(), key=lambda x: x[1], reverse=True)

        print(f"\nПовторення для послідовностей з {n} символів:")
        list1 = []
        for seq, freq in sorted_sequences:
            list1.append(seq)
        print(list1)
analyze_text(my_text)

