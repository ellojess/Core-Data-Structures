#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests

    # in-class walk through 
    # left_index = 0 
    # right_index = len(text) - 1
    # text = text.lower()

    # if text == "":
    #     return True
    

    # while left_index < right_index:
    #     if text[left_index] != text[right_index]: # not a palindrome 
    #         return False
    #     left_index += 1
    #     right_index -= 1
    # return True

    string = get_text(text)
    word = "" 

    for letter in reversed(string):
        word += letter
    if word == string:  
        return True
    return False


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    # base cases 
    if text == "":
        return True 

    if left == right or left > right:
        return True

    if left is None and right is None:
        left = 0
        right = len(text) - 1

    if text[left].lower() != text[right].lower(): # mismatch 
        return False 
    else: 
        # recursive case 
        return is_palindrome_recursive(text, left+1, right-1)


# helper function to handle white space, punctuation, and casing in text 
def get_text(text):
    lower_case = text.lower()
    no_white_space = lower_case.replace(" ", "")
    no_punctuation = no_white_space.translate(str.maketrans('', '', string.punctuation))
    return no_punctuation


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()