def remove_shared(L1, L2):
    '''(list, list)

    Remove items from L1 that are in L2. There is no return statement.

    >>> list_1 = [1, 2, 3, 4, 5, 6]
    >>> list_2 = [2, 4, 5, 7]
    >>> remove_shared(list_1, list_2)
    >>> list_1
    [1, 3, 6]
    >>> list_2
    [2, 4, 5, 7]
    '''

    for i in L2:
        if i in L1:
            L1.remove(i)
#
# L1a = [1,2,3]
# L2a = [1,2]
# remove_shared(L1a, L2a)
# print(L1a, L2a)
