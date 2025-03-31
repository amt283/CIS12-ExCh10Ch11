"""Write a function called most_frequent_letters that takes a string and prints the letters in decreasing order of
frequency.

To get the items in decreasing order, you can use reversed along with sorted or you can pass reverse=True as a keyword
parameter to sorted."""

def main():
    most_frequent_letters('mississippi')

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def most_frequent_letters(str_var):
    counts = value_counts(str_var)

    # Sort the letters based on frequency in decreasing order
    sorted_letters = sorted(counts.items(), key=lambda item: item[1], reverse=True)

    # Print the letters in order of decreasing frequency
    for letter, count in sorted_letters:
        print(f"Letter: {letter}, Count: {count}")

if __name__ == "__main__":
    main()