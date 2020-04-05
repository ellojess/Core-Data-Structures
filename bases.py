#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    digits = digits.lower() 
    characters = string.digits + string.ascii_lowercase
    decimal, i = 0,0
  
    # Decimal equivalent is str[len-1]*1 + str[len-1]*base + str[len-1]*(base^2) + ...  
    # loop through items in string from right to left 
    for digit in reversed(digits): 
        # Check if a digit in input number is less than number's base 
        if characters.find(digit) >= base:
            print("Invalid number")
            return -1
        # If input is valid, multiply item by the power of the base, add total values
        decimal += characters.find(digit) * pow(base, i)
        i += 1 
    return decimal

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    """
    Inverse decode 
    Convert int to base/radix 2-36 string
    Special numerals used to convert to any base or radix 
    """

    characters = string.digits + string.ascii_letters 

    if number < 0:
        sign = -1
    elif number == 0:
        return characters[0]
    else:
        sign = 1

    number *= sign
    digits = []

    """
    input number is given base  
    repeatedly divide by base and taking remainder 
    reverse results and join
    """
    while number:
        digits.append(characters[int(number % base)])
        number = int(number / base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # Convert digits from any base to any base (2 up to 36)
    return encode(decode(digits, base1), base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()