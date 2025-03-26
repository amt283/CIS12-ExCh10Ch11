"""What is the longest word you can think of where each letter appears only once? Let’s see if we can find one longer
than unpredictably.

Write a function named has_duplicates that takes a sequence – like a list or string – as a parameter and returns True
if there is any element that appears in the sequence more than once."""

def main():
    print(has_duplicates('unpredictably')) # False
    print(has_duplicates('mississippi')) # True
    print(has_duplicates('mice')) # False

def has_duplicates(string):
    counter = {}
    for letter in string:
        if counter.get(letter, 0) > 1:
            return True
        counter[letter] = counter.get(letter, 0) + 1
    return False

if __name__ == "__main__":
    main()