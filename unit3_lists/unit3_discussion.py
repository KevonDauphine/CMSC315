"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # When an insertion happens, python has to shift all the items at or after the insertion point
    # and can take O(n) time depending on the list
    lst.insert(index, value)
    pass


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Validation are important so data isn't lost or so the program doesn't crash

    if index < 0 or index >= len(lst): # if the index is below 0 or greater than the actual index, returns none, otherwise deletes the value at the index
        return None
    else:
        return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is linear because we search each element in order until the value is found

    for ind in range(len(lst)): # using for loop to look for the value in a list and then returning the index of the value, returns -1 when it isn't in the list
        if lst[ind] == value:
            return ind

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.
    print("\n=== INSERTION TESTS ===")

    num_list = [5,15,20] #making a list
    print(f"[insert test] Listing numbers: {num_list}")

    insert_at(num_list, 0, 0) #adding number to index 0 of list
    print(f" inserting number 0 at index 0: {num_list}")

    insert_at(num_list, 2, 10) # adding number to the middle of the list
    print(f" inserting number 10 at index 2: {num_list}")

    insert_at(num_list, len(num_list), 25) #adding number to the end of list
    print(f" inserting number 25 at end of index: {num_list}")



    # print("TODO: Create a list and demonstrate insertions.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    #print("TODO: Demonstrate deletions from multiple positions.")

    print(f"output before deletion {num_list}")
    first_num = delete_at(num_list, 0) # deleting the number to the first index of the list
    print(f" deleting number at index 0, {first_num}: {num_list}")

    middle_num = delete_at(num_list, len(num_list) // 2) #using math to delete the middle number of a list
    print(f" deleting middle number, {middle_num}: {num_list}")

    end_num  = delete_at(num_list, len(num_list) - 1) #deleting last number of a list
    print(f" deleting number at end of index, {end_num}: {num_list}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    print(f"Searching for existing value 20 and non existing 50. Current list -> {num_list}")
    exist_num = search_value(num_list, 20) # using a known existing number as a value
    nonexist_num = search_value(num_list, 50) # using a known non-existing number as a value to not find

    print(f"found 20 at index {exist_num}: 50 returns {nonexist_num}, does not exist in list")

    #print("TODO: Demonstrate searching for values.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    print(f"deleting in list: {num_list} with out of bounds index of 100") #edge case showcasing the safe operation of trying to use an out-of-bounds index
    edge_del = delete_at(num_list, 100)
    print(f"returns value: {edge_del}: printing list -> {num_list}")

    print(f"Searching for missing value, 16.") # searching for a value that doesn't exist
    missing = search_value(num_list, 16)
    print(f"found 16 at index {missing}, doesn't exist: {num_list}")

    new_list = [] # Making a new list, then adding to it
    print(f"Making empty list: {new_list}")
    insert_at(new_list, 0, 0)

    print(f"inserting value into new list: {new_list}")

    new_new_list = [] #making a new list to show what happens when you delete from an empty list
    print(f"Making new empty list: {new_new_list}")
    new_del = delete_at(new_new_list, len(new_new_list))
    print(f"deleting from new empty list: {new_del}: printing list -> {new_new_list}")


    #print("TODO: Demonstrate at least two edge cases.")

    # ===============================
    # Real world example
    # ===============================


    # Making a list of customers to be added and removed from a list
    print("Making a list for customers at a Line")
    customer_list = ["Lisa", "Kevin", "John"]
    print(f"customer list: {customer_list}")

    insert_at(customer_list, 0, "Smith")
    print(f"adding new customer, Smith. To the list - > {customer_list}")

    delete_at(customer_list, search_value(customer_list, "Lisa"))
    print(f"Customer conclusion reached, removing Lisa -> {customer_list}")

if __name__ == "__main__":
    main()