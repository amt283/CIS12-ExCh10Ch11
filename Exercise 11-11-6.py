"""Write a function called word_distance that takes two words with the same length and returns the number of places
where the two words differ.

Hint: Use zip to loop through the corresponding letters of the words."""

def main():
    print(word_distance("final", "finally"))  # Error
    print(word_distance("grate", "plate"))  # 2

def word_distance(word1, word2):
    count = 0

    # Check that words are the same length & use zip to pair letters from both words
    # then count where the letters differ
    if len(word1) == len(word2):
        for first, second in zip(word1, word2):
            if first != second:
                count += 1
        return count
    else:
        return f"\"{word1.capitalize()}\" and \"{word2.capitalize()}\" are not the same length!"

if __name__ == "__main__":
    main()