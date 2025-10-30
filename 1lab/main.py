

if __name__ == "__main__":
    text = input("Введите строку: ")
    text = text.lower()

    symbols_to_remove = ",.!?;:-\"'()[]{}"
    for symbol in symbols_to_remove:
        text = text.replace(symbol, "")

    words = text.split()

    letters = [ch for ch in text if ch.isalpha()]

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    letter_freq = {}
    for letter in letters:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1

    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse = True)
    sorted_letters = sorted(letter_freq.items(), key=lambda x: x[1], reverse = True)

    print("Топ 5 слов:")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

    print("Топ 5 букв:")
    for letter, count in sorted_letters[:5]:
        print(f"{letter}: {count}")
