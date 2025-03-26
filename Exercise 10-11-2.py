'''Use "get" to write a more concise version of value_counts. You should be able to eliminate the "if" statement.'''

def main():
    string_w = "banana"
    print(get_value_counts(string_w)) # Should return b = 1, a = 3, n = 2
    test_dict = get_value_counts(string_w)
    print(test_dict.get('a', 0)) # Should return 3

# The new value_counts function with the "get" statement
def get_value_counts(string):
    counter = {}
    for letter in string:
        # duplicate keys in dict not possible, if it doesn't exist it adds and makes the value 0,
        # if it does it overwrites previous value and adds 1
        counter[letter] = counter.get(letter, 0) + 1
    return counter

# The original value_counts function with the "if" statement
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

if __name__ == "__main__":
    main()