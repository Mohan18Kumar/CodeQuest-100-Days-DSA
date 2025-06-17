def word_frequency(sent):
    sent = sent.lower()
    words = sent.split()
    freq_map = {}

    for word in words :
        if word in freq_map:
            freq_map[word] += 1
        else:
            freq_map[word] = 1
    for word, count in freq_map.items():

        print(f"{word}: {count}")
input_sent = input ("Enter a sentence: ")
word_frequency(input_sent)