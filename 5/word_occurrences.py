def main():
    text = input("Text: ")
    word_calculate = calcu_words(text)
    print_word_counts(word_calculate)

def calcu_words(text):
    words = text.split()
    word_calculate = {}
    for word in words:
        word = word.lower()
        if word in word_calculate:
            word_calculate[word] += 1
        else:
            word_calculate[word] = 1
    return word_calculate

def print_word_counts(word_calculate):
    sorted_words = sorted(word_calculate.keys())
    max_length = max(len(word) for word in sorted_words)
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_calculate[word]}")

main()

##Word Occurrences Estimate:20 mins, Actual:47mins