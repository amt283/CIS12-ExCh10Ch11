"""Write a function called add_counters that takes two dictionaries like this and returns a new dictionary that
contains all of the letters and the total number of times they appear in either word."""

def main():
    counter1 = get_value_counts('pronto')
    counter2 = get_value_counts('photoreal')
    print(add_counters(counter1, counter2)) # p = 2, o = 4, t = 2, r = 2

# adds values of common keys together from two dicts and returns a new dict with the sum
def add_counters(dict1, dict2):
    dict_sum = {}
    for key in dict2:
        if key in dict1:
            dict_sum[key] = dict2[key] + dict1[key]
    return dict_sum

# loops through string and returns a dict with letters in str as keys and count of times letter is used as value
def get_value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

if __name__ == "__main__":
    main()