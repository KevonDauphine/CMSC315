import time
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # A linear search has to go from index 0 to end. Meaning a linear search has to check every single value to make sure
    # it's there. In worse cases such as max value or for values not even in the list, a linear search would have to
    # look through every element, giving it O(n) time as the list grows with more items.

    for index in range(len(lst)): # runs through the elements of the list
        if lst[index] == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # A binary search goes to the middle of the index, checking if the value is greater or less than this middle number
    # to basically cut out one half of the list depending on the value on sorted list. Cutting the list in half
    # splits the number of operations in half, giving binary search O(log n) time

    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (high + low) // 2
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    #print("TODO: Create a small dataset and test both searches.")

    small_data = [5, 10, 15, 20, 25, 30, 35] # Small list of numbers
    value = 10
    print(f"List of numbers: {small_data}. \nNumber we are looking for is {value}")

    # linear search
    start_time = time.time()
    linear_result = linear_search(small_data, value)
    print(f"\nresults of linear result: {linear_result}")
    print(f"Linear Time elapsed: {time.time() - start_time}")
    # Since this list isn't big, linear search takes no time at all to find values

    # binary search
    start_time = time.time()
    binary_result = binary_search(small_data, value)
    print(f"\nresults of binary result: {binary_result}")
    print(f"\nBinary Time elapsed: {time.time() - start_time}")
    print("\nNow looking for a value that does not exist for both searches")
    # since the list isn't big, linear may be faster or similar speed

    value = 900
    start_time = time.time()
    linear_result = linear_search(small_data, value)
    print(f"\nresults of linear result of value that doesn't exist, {value}: {linear_result}")
    print(f"Linear Time elapsed: {time.time() - start_time}")
    # Linear had to do a worst cast search since this value does not exist, searching from index 0 to the end.


    start_time = time.time()
    binary_result = binary_search(small_data, value)
    print(f"\nresults of binary result that doesn't exist, {value}: {binary_result}")
    print(f"Binary Time elapsed: {time.time() - start_time}")
    # Binary cuts the list and half and just searches from the halfway point, cutting the time it would take a linear search

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # large list created
    large_data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 75, 80, 85, 90, 95, 100,
                  105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200,
                  205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305,
                  310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400,
                  405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490,
                  495, 500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 600,
                  605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 680, 685, 690, 695, 700,
                  705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790, 800]

    lvalue = 500
    print(f"\nList of numbers: {large_data}. \nNumber we are looking for: {lvalue}")

    # binary search
    start_time = time.time()
    binary_lresult = binary_search(large_data, lvalue)
    print(f"\nresults of binary result: {binary_lresult}")

    # time it took
    print(f"Binary Time elapsed: {time.time() - start_time}")
    # Since Binary search isn't starting at index 0, it will take much less time because the search starts at halfway as data gets larger

    # linear search
    start_time = time.time()
    linear_lresult = linear_search(large_data, lvalue)
    print(f"\nresults of linear result: {linear_lresult}")

    # time it took for linear search
    print(f"Linear Time elapsed: {time.time() - start_time}")
    # With linear always starting at index 0. This way of searching becomes inefficient and it shows in the results of time
    # and would show even more if I had more and more data to this set.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty_list = [] # empty list edge test
    empty_result = linear_search(empty_list, 5)
    print(f"\nmade empty list: {empty_list}")
    print(f"searched 5 in list, results of empty result should return -1 since list is empty: {empty_result}")

    value_list = ["Cat", "Dog", "Horse"]
    value_result = binary_search(value_list, "Cat")
    print(f"\nlist of animals: {value_list}")
    print(f"\nSearching for \"cat\" to test for edge case of first position value:\nresult of cat should should return 0: {value_result}")


if __name__ == "__main__":
    main()