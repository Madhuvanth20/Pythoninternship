# -*- coding: utf-8 -*-

from collections import Counter

def count_unique_words(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            words = data.split()
            word_count = Counter(words)
            return word_count

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def main():
    file_path = "C:\\Users\\madhu\\Desktop\\python\\task1(1)\\names.txt" 
    word_count = count_unique_words(file_path)

    if word_count is not None:
        print("Unique words and their occurrences:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()

