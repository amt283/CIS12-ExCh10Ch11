"""Write a function called shift_word that takes as parameters a string and an integer, and returns a new string that
contains the letters from the string shifted by the given number of places.

To test your function, confirm that “cheer” shifted by 7 is “jolly” and “melon” shifted by 16 is “cubed”.

Hints: Use the modulus operator to wrap around from 'z' back to 'a'. Loop through the letters of the word, shift each
one, and append the result to a list of letters. Then use join to concatenate the letters into a string."""

def main():
    print(shift_word('cheer', 7)) # jolly
    print(shift_word('melon', 16)) # cubed

def shift_word(str_var, shift_int):
    # Create a dictionary that maps from each letter to its index in the alphabet.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range(len(letters))
    letter_map = dict(zip(letters, numbers))

    caesar_word = []

    # Loop through string and shift the letter based on the shift_int
    # % 26 used to loop back to 'a' when 'z' is reached
    for letter in str_var:
        new_index = (letter_map[letter] + shift_int) % 26
        caesar_word.append(letters[new_index])
    return ''.join(caesar_word)

if __name__ == "__main__":
    main()