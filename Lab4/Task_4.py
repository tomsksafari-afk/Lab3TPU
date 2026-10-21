words = ["apple", "book", "computer", "book", "cat"]

word_lengths_loop = {}

for word in words:
    word_lengths_loop[word] = len(word)

print(word_lengths_loop)

word_lengths_comp = {word: len(word) for word in words}

print(word_lengths_comp)