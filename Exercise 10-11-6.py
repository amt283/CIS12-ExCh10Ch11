"""Write a function called add_counters that takes two dictionaries like this and returns a new dictionary that
contains all of the letters and the total number of times they appear in either word."""
import nltk

def main():
    # Downloads dictionary word package for is_english function, not needed every time
    #nltk.download('words')
    print(is_interlocking('schooled')) # True
    print(is_interlocking('wrong')) # False
    print(is_interlocking('shoow')) # False

# Returns true if word is interlocking (every other letter makes two new words)
def is_interlocking(word):
    first = word[0:None:2]
    second = word[1::2]
    if is_english(word) and is_english(first) and is_english(second):
        return True
    return False

#Checks whether string is a word in English
def is_english(word):
    english_words = set(nltk.corpus.words.words())
    return word.lower() in english_words

if __name__ == "__main__":
    main()