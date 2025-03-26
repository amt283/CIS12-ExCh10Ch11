"""Write function called find_repeats that takes a dictionary that maps from each key to a counter, like the result
from value_counts. It should loop through the dictionary and return a list of keys that have counts greater than 1."""

def main():
    str_word = "mississippi"
    value_count = get_value_counts(str_word)
    print(value_count) # m = 1, i = 4, s = 4, p = 2
    print(find_repeats(value_count)) # List with "i", "s" and "p"

def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    key_list = []
    # loops through keys and values in dict, .items() needed to loop through both
    for key, value in counter.items():
        if value > 1:
            key_list.append(key)
    return key_list

# loops through string and returns a dict with letters in str as keys and count of times letter is used as value
def get_value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

if __name__ == "__main__":
    main()