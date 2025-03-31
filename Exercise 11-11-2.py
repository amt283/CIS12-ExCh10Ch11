"""Write a line of code that appends the value 6 to the end of the second list in t. If you display t, the result
should be ([1, 2, 3], [4, 5, 6]).

Try to create a dictionary that maps from t to a string, and confirm that you get a TypeError."""


def main():
    list0 = [1, 2, 3]
    list1 = [4, 5]
    list2 = [6]

    t = (list0, list1)
    new_t = (list0, list1 + list2)
    print(new_t)

    # d = {t: 'this tuple contains two lists'}
    # print(d)


if __name__ == "__main__":
    main()