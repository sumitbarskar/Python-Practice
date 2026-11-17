set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

# Elements that are NOT common in both sets
result = set_a.symmetric_difference(set_b)

print("Set A:", sorted(set_a))
print("Set B:", sorted(set_b))
print("Symmetric Difference:", sorted(result))
