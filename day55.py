numbers = {10, 20, 10, 30, 20, 40, 50}

print("Original Set:", sorted(numbers))

# Add an element
numbers.add(60)
print("After Adding 60:", sorted(numbers))

# Remove an element
numbers.remove(30)
print("After Removing 30:", sorted(numbers))

# Check if an element exists
if 20 in numbers:
    print("20 is present in the set")
else:
    print("20 is not present in the set")
