# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## My Reflection
While doing this assignment, I learned how binary search trees (BST) actually work. 
I got a lot more comfortable with recursion too after awhile things clicked and I managed to get it down!

A challenge I ran into was writing the recursive insert and search methods correctly the first time. 
My first attempt at insert only checked the first level and overwrote existing nodes instead of recursing deeper when a spot was already taken. 
My first search attempt also forgot to check if the current node matched before recursing further, 
and had no check for hitting an empty node, which caused a crash. Fixing both came down to making sure I had a real base case and only recursed when actually needed.

BSTs stay ordered by putting smaller values left and larger values right, 
so each comparison during search cuts the remaining space roughly in half, 
giving O(log n) search instead of checking every item like a list does. But that only holds if the tree stays balanced. 
I tested this myself, inserting values already sorted turned the tree into basically a straight line, height 7 instead of 3, making search just as slow as a list.