def collect_vowels(s):
    '''(str) -> str

    Return the vowels (a, e, i ,o ,u) from s.

    >>> collect_vowels('Happy Anniversary')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    '''

    vowels = ''

    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels


def count_vowels(s):
    '''(str) -> int

    Return the number of vowels (a, e, i ,o ,u) in s.

    >>> count_vowels('Happy Anniversary')
    'aAiea'
    >>> count_vowels('xyz')
    ''
    '''

    num_vowels = 0

    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1


def get_divisors(num, possible_divisors):
    ''' (int, list of int) -> list of int

    Return a list of the values from possible_divisors
    that are divisors of num.

    >>> get_divisors(8, [1, 2, 3])
    [1, 2]
    >>> get_divisors(4, [-2, 0, 2])
    [-2, 2]
    '''

    divisors = []
    for item in possible_divisors:
        if item != 0 and num % item == 0:
            divisors.append(item)

    return divisors


def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''

    # For each character in s, add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev

    return rev


def is_palindrome_v1(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """

    return reverse(s) == s


def is_palindrome_v2(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """

    # The number of chars in s.
    n = len(s)

    # Compare the first half of s to the reverse of the second half.
    # Omit the middle character of an odd-length string.
    return s[:n // 2] == reverse(s[n - n // 2:])


