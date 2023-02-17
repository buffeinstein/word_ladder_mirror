# Word Ladders with Stacks and Queues
[![](https://github.com/buffeinstein/cs46hw03-word_ladder/workflows/tests/badge.svg)](https://github.com/buffeinstein/cs46hw03-word_ladder/actions?query=workflow%3Atests)

You will implement a solution to Lewis Carroll's [word ladder game](https://en.wikipedia.org/wiki/Word_ladder).

**Learning Objectives:**

1. implement a complex algorithm involving both queues and stacks
1. understand python memory management
1. practice translating pseudocode into python

**Relation to technical interviews:**

[Leetcode](https://leetcode.com/problemset/all/) is a common method used for technical interviews.
The world ladder problem is an example of a problem that leetcode puts in their hardest-to-solve category (see [the problem description on leetcode.com](https://leetcode.com/problems/word-ladder/)).
What makes these problems "hard" is figuring out the right pseudocode.
Translating from pseudocode into working code is considered "easy".

In this assignment, we will practice the translation of pseudocode into working python code.
If you want to learn more about how to create the pseudocode in the first place,
then you should take CSCI148: Graph Algorithms with Prof Sarah Cannon.

## Background

A word ladder is a list of words where each word differs by only a single letter from the previous word.
For example, we can convert a `stone` into `money` using the following ladder:

```
stone
shone
shote
shots
soots
moots
motts
motes
motey
money
```

In this assignment, you will implement a function `word_ladder` that generates these word ladders.
There are many possible algorithms to generate word ladders,
but a simple one uses a combination of stacks and queues as shown in the following pseudocode.

```
Create a stack
Push the start word onto the stack
Create a queue
Enqueue the stack onto the queue

While the queue is not empty
    Dequeue a stack from the queue
    For each word in the dictionary
        If the word is adjacent to the top of the stack
            If this word is the end word
                You are done!
                The front stack plus this word is your word ladder.
            Make a copy of the stack
            Push the found word onto the copy
            Enqueue the copy
            Delete word from the dictionary
```

**HINTs:**

1. This pseudocode is intentionally vague,
   and I encourage you to ask clarifying questions.
   The ability to ask good questions is one of the keys skills being tested in technical interviews.

1. One of the main differences between pseudocode and real code is that pseudocode doesn't have to deal with memory management, but real code does.
   The vast majority of bugs that students get with this assignment is due to memory management issues.

1. The test cases take a long time to run, and you will not be efficient if you are re-running them all the time.
   Instead, use the `--last-failed` flag in pytest to skip the tests that you have previously passed and only run the failing tests.

## Tasks

Complete the following tasks:

1. Fork this repo and enable github actions
1. Update the `README.md` file so that the travis button points to your repo
1. Implement the `word_ladder`, `verify_word_ladder`, and `_adjacent` functions so that all test cases in `tests/test_main.py` pass

If all test cases pass, you will get full credit.
If not all test cases pass, you will lose -4 points for the first failing test case and -1 points for each additional failing test case.

## Submission

Submit the link to your forked repository on sakai.
