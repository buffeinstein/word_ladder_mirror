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
                    #what this code will fix:
                    #test__word_ladder_9
                    #test__word_ladder_8
                    #test__word_ladder_10
                    #what it won't:
                    #test__word_ladder_7 will not be fixed with this
                    #test__word_ladder_fuzz is interesting
                    #it tests if the lengths match of list from going
                    #forwards vs backwards from the same 2 words 
                    #sometimes-  the length is the same because they
                    #will be reversed lists (ggod)
                    #other times - the list lenths match, but 
                    #not the lists themselves (bad?)
                    #what this code is fixing:
                    #many times - the lists have one too many words
                    #in going from higher alphabetical to lower
                    #alphabetical, the ladder will have an unneccessary 
                    #step
                    #ex: 'crone', 'clone', 'clonk',x, 'clons', 'clops',
                    #vs:'clops', 'clons', 'clone', 'crone'
                    #due to the use of the for loop that goes
                    #through an alphabetized dict
                    #thus, we can use code similar to the adjacent func
                    #this takes a list and trims it 
                    current2 = current [:]
                    for i in range(len(current) - 2):
                        if _adjacent(current[i],current[i + 2]):
                            current2.remove(current[i+1])
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
