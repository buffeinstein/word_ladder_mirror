#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
#    if start_word == end_word:
#        return [start_word]
#    
#    dictionary = []
#    with open (dictionary_file, 'r') as f: 
#        text = f.read()
#    dictionary = text.split() 
#
#    stack = [start_word]
#
#    while stack[-1] != end_word: 
#        for word in dictionary: 
#            if _adjacent(word, stack[-1]) and word not in stack:
#                if word == end_word: 
#                    stack.append(word) 
#                    return stack
#                else: 
#                    stack.append(word)
#                    dictionary.remove(word)
#                    found_adjacent = True 
#        if not found_adjacent:
#            return None


# lets go over why ^ this code doesn't work
# we have only one stack here. this means we're giving 
#ourselves the option to create only one path. and the choices
#for our next step are determined without logic, just by the chance
#of stumbling onto something that is adjacent by going alphabetically 
#(as we're looping thru a dict). 
#instead - we should give ourselves as many paths as possible. for example: 
#lets say our start word is "shone". our end word is "story". our dict = 
#[shone, phone, stone, stony, story]. 
#we can see that we can do [shone, stone, stony, story], but ^ that code will
#find phone first, and be stuck. 
#instead - we should let the code explore the different ways to get to 
#story. what if we could create all possible ladders, and take one step
#on each path before deciding which one to continue on?
#this would look like adding all adjacent words to our start word, [

    with open (dictionary_file, 'r') as f: 
        text = f.read()
    dictionary = text.split() 
    
    
    if start_word == end_word: 
        return [start_word]
    stack1 = [start_word]
    q = deque([])
    q.append(stack1)
    dictionary.remove(start_word)
    #this sets us up to build our first ladder. however, the queue can store 
    #multiple ladders - all the different paths to our end word 
    #its important that we do a queue of lists, so that we can 
    #take off the left end  - i'll explain why this is important later 

    while len(q)>0: 
        #why would this be empty? because we're popping left to get the new 
        #possible ladder to work on. if this is empty, we have exhausted all 
        #of our variations of the ladder - there is no possible 
        #way to get to the end
        current = q.popleft()
        #this is already a list
        for w in dictionary: 
            if _adjacent(w, current[-1]) and w not in current: 
                if w == end_word: 
                    current.append(w)
                    return current
                nextt = copy.copy(current)
                nextt.append(w)
                q.append(nextt)
                
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
    for i in range(len(ladder)-1):
        if not _adjacent(ladder[i], ladder[i+1]):
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











