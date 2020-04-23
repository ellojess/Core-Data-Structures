#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    if find_index(text, pattern) is not None:
        return True
    else: 
        return False



def find_index(text, pattern, start = 0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    """
    - loop through text to find pattern 
    - compare pattern value and text value 
    - return index or none 
    """
    
    # check if pattern is empty 
    if pattern == '':
        return 0 
    if pattern == text:
        return 0
    if len(pattern) > len(text):
        return None 

    # loop from start to end of 
    for index in range(start, len(text) - len(pattern) + 1):
        if text[index] == pattern[0]: # text and pattern match at first value 
            if text[index: index + len(pattern)] == pattern: # text and pattern match at subsequent value
                return index
    return None
    

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    indexes = [] 
    i = find_index(text, pattern)

    # base cases, check if pattern is empty & edge case with empty string
    if pattern == "":
        for i in range(len(text)):
            indexes.append(i)
        return indexes

    if pattern == text:
        return [0]

    if i is not None:
        indexes.append(i)
    else:
        return indexes

    for index in indexes:
        i = find_index(text, pattern, index + 1)
        if i is not None and i < len(text):
            indexes.append(i)
        else:
            break   
    return indexes

    # Jess' walk through 
    # all_indexes = []

    # if pattern == "":
    #     for i in range(len(text)):
    #         all_indexes.append(i)
    #     return all_indexes

    # for text_index in range(len(text)):
    #     text_letter = text[text_index]
    #     #check if letter is start of pattern 
    #     if text_letter == pattern[0]:
    #         for pattern_index in range(len(pattern)): 
    #             if pattern[pattern_index] != text[text_index + pattern_index]:
    #                 break
    #             if pattern_index == len(pattern) - 1:
    #                 all_indexes.append(text_index)





def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()