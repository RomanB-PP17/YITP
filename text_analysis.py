import string
from collections import Counter
import matplotlib.pyplot as plt

def get_alphabet(text):
    """Отримує алфавіт (унікальні символи) у тексті."""
    return sorted(set(text))

def get_char_frequencies(text):
    """Рахує частоти символів у тексті."""
    return Counter(text)

def get_bigrams(text):
    """Рахує біграми у тексті."""
    bigrams = [text[i:i + 2] for i in range(len(text) - 1)]
    return Counter(bigrams)

def get_trigrams(text):
    """Рахує тріграми у тексті."""
    trigrams = [text[i:i + 3] for i in range(len(text) - 2)]
    return Counter(trigrams)

def filter_text(text):
    """Фільтрує текст, залишаючи лише допустимі символи."""
    allowed_chars = string.ascii_letters + string.digits + string.punctuation + " "
    return ''.join([char for char in text if char in allowed_chars]).replace(' ', '_')

def plot_histogram(freqs, title):
    """Будує гістограму частот символів або біграм."""
    if not freqs:
        return
    chars, counts = zip(*freqs)
    plt.figure(figsize=(12, 6))
    plt.bar(chars, counts, color='yellow')
    plt.title(title)
    plt.xlabel('Символи')
    plt.ylabel('Частота')
    plt.show()
