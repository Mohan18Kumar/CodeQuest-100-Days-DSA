def main():
    sentence = input("Enter a sentence: ").strip().lower()

    words = sentence.split()

    frequency_map = {}

    for word in words:
        if word in frequency_map:
            frequency_map[word] += 1
        else:
            frequency_map[word] = 1

    print("Word Frequencies:")
    for word, count in frequency_map.items():
        print(f"{word}: {count}")

if __name__ == "_main_":
    main()