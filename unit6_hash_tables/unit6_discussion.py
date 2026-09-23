"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    loot_table = {"Pistol": {"Damage": 10, "Rarity": "Common", "Cost": 5},
                  "Laser": {"Damage": 50, "Rarity": "Rare", "Cost": 500},
                  "Sword": {"Damage": 25, "Rarity": "Uncommon", "Cost": 125},
                  "Beam Sword": {"Damage": 8050, "Rarity": "Epic", "Cost": 7500},
                  "Orbital Cannon": {"Damage": 99999, "Rarity": "Unique", "Cost": 50000}}  # making hash table

    # Like a hash table, dictionaries use hash functions to determine key value pairs in a table and map it directly to its value.

    print(loot_table)



    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    key1 = loot_table["Pistol"]
    key2 = loot_table["Laser"]
    print(f"key1 Pistol: {key1} \nkey2 Laser: {key2}") #looks for the value by passing in a key to calculate the index where the value is stored


    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print(f"Changing the damage of Pistol {key1} to 15")
    loot_table["Pistol"] = {"Damage": 15, "Rarity": "Common", "Cost": 5}
    key1 = loot_table["Pistol"]
    print(f"Damage changed {key1}") # new values of existing keys overwrite the old in the hash table

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.
    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    print("Dictionary before deletion")

    for key, value in loot_table.items():
        print(f"Weapon: {key} \n - value: {value["Damage"]} \n - Rarity {value['Rarity']} \n - Cost {value['Cost']}")
        print("---" * 10)

    del loot_table["Beam Sword"]

    print("Dictionary before After deletion")

    for key, value in loot_table.items():
        print(f"Weapon: {key} \n - value: {value["Damage"]} \n - Rarity {value['Rarity']} \n - Cost {value['Cost']}")
        print("---" * 10)




    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: looking up a key that doesn't exist.
    # Using square brackets (loot_table["Rocket Launcher"]) would raise a
    # KeyError and crash the program. Using .get() instead returns None safely
    # if the key isn't found, since it doesn't assume the key exists.
    missing_weapon = loot_table.get("Rocket Launcher")
    print(f"Looking up 'Rocket Launcher' (does not exist): {missing_weapon}")

    # Edge case 2: deleting a key that doesn't exist.
    # Using del loot_table["Rocket Launcher"] would raise a KeyError and crash.
    # Using .pop() with a default value returns that default instead of
    # crashing if the key isn't found.
    removed = loot_table.pop("Rocket Launcher", "Key not found")
    print(f"Attempting to delete 'Rocket Launcher' (does not exist): {removed}")





if __name__ == "__main__":
    main()