'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base cases:
    if len(word) <= 2:
        if word == 'th':  # if it's two characters, see if they match
            return 1
        else:            # if it's less characters or they don't match, test fails
            return 0

    # check the next two characters and pass on the rest
    return count_th(word[:2]) + count_th(word[1:])
