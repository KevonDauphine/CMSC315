# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## My Reflection

While doing this assignment, I learned how insertion, deletion, and search actually affect how a Python list performs. 
I used a travel itinerary as my real-world example since activities get added, removed, and searched for as plans change. 
I learned that if you insert something near the beginning or middle of a list, everything after it has to shift to the right to make room. 
Deleting works the same way but backwards everything shifts left to fill the gap. So depending on where in the list you're making the change, these operations can end up taking O(n) time.

A challenge I ran into was making sure I handled invalid indexes and empty lists without crashing. 
I fixed this by checking if the index was valid before trying to delete anything, 
and just returning None if that position didn't actually exist. 
I also built a linear search that goes through the list one item at a time and returns -1 if it never finds the value.

For real-world use, list performance starts to matter a lot more once the data gets bigger. 
Adding and removing items a lot can get expensive since elements keep having to shift around. 
Understanding this stuff helps you actually pick the right data structure instead of just using a list for everything.