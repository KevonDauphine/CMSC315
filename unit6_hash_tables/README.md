# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## My reflection
While doing this assignment, I learned how Python dictionaries work as hash tables under the hood, not just as a way to store data. 
I built a loot table for a game using weapon names as keys and stats like damage and rarity as values, 
which made insert, lookup, update, and delete all feel natural since dictionaries are built for exactly that.
Hash tables work by running each key through a hash function that points directly to where its value is stored, 
giving lookups O(1) time instead of searching through everything. A collision happens when two different keys hash to the same location, 
and when that happens the table has to check multiple entries at that spot instead of landing directly on one, 
slowing lookups down toward O(n) in the worst case.