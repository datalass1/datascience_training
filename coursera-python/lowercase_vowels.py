def count_lowercase_vowels(s):
    '''(str)-> str

    Return the number of vowels (a,e,i,o,u) in a string

    >>> count_lowercase_vowels('Happy Birthday')
    3
    >>> count_lowercase_vowels('xyz')
    0
    '''

    num_vowels = 0

    for char in s:
        if char in 'aeiou':
            num_vowels = num_vowels + 1

    return num_vowels
