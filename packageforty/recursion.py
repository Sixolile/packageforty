def sum_array(array):

    '''Return sum of all items in array'''
    added = 0
    for x in array:
        added = x + array
    return added

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


    '''Return nth term in fibonacci sequence'''

def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    '''Return n!'''

def reverse(word):
    rev_word = ''
    for x in word:
        rev_word = x + rev_word
    '''Return word in reverse'''
