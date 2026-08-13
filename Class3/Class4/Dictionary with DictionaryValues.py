# ===== Basic Nested Dictionaries =====
d2 = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
d3 = {'c': {'x': 5, 'y': 6}, 'd': {'x': 7, 'y': 8}}
d4 = {'outer': {'key': 'value'}}

d5 = {'People1': {'name': 'Jack', 'id': 420}}
d5['people2'] = {'name': 'Ramana', 'id': 421}

print("=" * 50)
print("EXAMPLE 1: Basic Nested Dictionaries")
print("=" * 50)
print("d2:", d2)
print("d3:", d3)
print("d4:", d4)
print("d5:", d5)

# ===== Example 2: Iterating through nested dictionaries =====
print("\n" + "=" * 50)
print("EXAMPLE 2: Iterating Nested Dictionary Values")
print("=" * 50)

d = {'emp1': {'name': 'Rocky', 'id': 555}}
print("d:", d)

print("\nIterating d2:")
for key, value in d2.items():
    print(f"  Outer key: {key}, Inner dict: {value}")

print("\nIterating d5:")
for key, value in d5.items():
    print(f"  Key: {key}")
    for inner_key, inner_value in value.items():
        print(f"    {inner_key}: {inner_value}")

# ===== Example 3: Printing deeply nested dictionaries =====
print("\n" + "=" * 50)
print("EXAMPLE 3: Printing Deeply Nested Dictionary")
print("=" * 50)

def print_nested_dict(dct, parent_key="", indent=0):
    """Recursively print nested dictionaries"""
    for k, v in dct.items():
        if isinstance(v, dict):
            print("  " * indent + f"{parent_key}{k}:")
            print_nested_dict(v, "", indent + 1)
        else:
            print("  " * indent + f"{parent_key}{k}: {v}")

print("Deeply nested dictionary d5:")
print_nested_dict(d5)

# ===== Example 4: Collecting all values from nested dict =====
print("\n" + "=" * 50)
print("EXAMPLE 4: Collecting All Values from d2")
print("=" * 50)

all_values = []
for value in d2.values():
    if isinstance(value, dict):
        all_values.extend(value.values())
print("All values in d2:", all_values)

# ===== Example 5: Flattening nested dictionary =====
print("\n" + "=" * 50)
print("EXAMPLE 5: Flattening Nested Dictionary (d3)")
print("=" * 50)

flat_d3 = {
    f"{outer_key}_{inner_key}": inner_value 
    for outer_key, inner_dict in d3.items() 
    for inner_key, inner_value in inner_dict.items()
}
print("Flattened d3:", flat_d3)

# ===== Example 6: Accessing nested dictionary values =====
print("\n" + "=" * 50)
print("EXAMPLE 6: Accessing Nested Dictionary Values")
print("=" * 50)

print("d4['outer']['key']:", d4['outer']['key'])
print("d5['People1']['name']:", d5['People1']['name'])
print("d5['people2']['id']:", d5['people2']['id'])

# ===== Example 7: Merging dictionaries =====
print("\n" + "=" * 50)
print("EXAMPLE 7: Merging Nested Dictionaries")
print("=" * 50)

d_merged = {**d2, **d3}
print("Merged d2 and d3:", d_merged)

# ===== Example 8: Updating nested values =====
print("\n" + "=" * 50)
print("EXAMPLE 8: Updating Nested Dictionary Values")
print("=" * 50)

print("Original d5:", d5)
d5['People1']['age'] = 25
d5['people2'].update({'city': 'New York', 'age': 30})
print("Updated d5:", d5)

# ===== Example 9: Checking if keys exist =====
print("\n" + "=" * 50)
print("EXAMPLE 9: Checking If Keys Exist in Nested Dict")
print("=" * 50)

if 'outer' in d4:
    print("'outer' key found in d4:", d4['outer'])

if 'People1' in d5 and 'name' in d5['People1']:
    print("Found name in d5['People1']:", d5['People1']['name'])

# ===== Example 10: Deleting from nested dictionary =====
print("\n" + "=" * 50)
print("EXAMPLE 10: Deleting Nested Dictionary Values")
print("=" * 50)

d_test = {'a': {'x': 1, 'y': 2, 'z': 3}, 'b': {'p': 4}}
print("Before deletion:", d_test)
del d_test['a']['y']
print("After deleting d_test['a']['y']:", d_test)