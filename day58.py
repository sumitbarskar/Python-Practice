# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "AIML",
    "marks": 85
}

# Accessing dictionary values
print("Student Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

# Updating a value
student["marks"] = 90

# Adding a new key-value pair
student["city"] = "Bhopal"

print("\nUpdated Student Details:")
print(student)
