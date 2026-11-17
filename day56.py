set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

# Union: Combine both sets
print("Union:", sorted(set_a.union(set_b)))

# Intersection: Common elements
print("Intersection:", sorted(set_a.intersection(set_b)))

# Difference: Elements present in A but not in B
print("Difference (A - B):", sorted(set_a.difference(set_b)))

# Difference: Elements present in B but not in A
print("Difference (B - A):", sorted(set_b.difference(set_a)))
