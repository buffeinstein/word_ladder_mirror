#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    with open(dictionary_file, 'r') as f:
        text = f.read()
    dictionary = text.split()
    if len(start_word) != len(end_word):
        return None

    if start_word == end_word:
        return [start_word]

    stack1 = [start_word]
    q = deque()
    q.append(stack1)
    dictionary.remove(start_word)

    while len(q) > 0:
        current = q.popleft()
        for w in dictionary:
            if _adjacent(w, current[-1]) and w not in current:
                if w == end_word:
                    current.append(w)
                    current2 = current[:]
                    for i in range(len(current) - 2):
                        if _adjacent(current[i], current[i + 2]):
                            current2.remove(current[i + 1])
                    print(current2)
                    return current2
                nextt = copy.copy(current)
                nextt.append(w)
                q.append(nextt)
                dictionary.remove(w)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    if len(ladder) == 1:
        return True
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    lst1 = []
    lst2 = []
    diff = 0
    for i, char in enumerate(word1):
        lst1.append(char)
    for i, char in enumerate(word2):
        lst2.append(char)
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            diff += 1
    return diff == 1
