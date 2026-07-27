math = ("Mathematics", "Mr. Sharma", 5, "Monday")
science = ("Science", "Ms. Priya", 4, "Wednesday")

print("Subject 1:", math)
print("Name:", math[0])
print("Teacher:", math[1])
print("Day:", math[-1])

all_subjects = (math, science)

print("\nFirst subject name:", all_subjects[0][0])
print("Second subject periods:", all_subjects[1][2])
print("Math details (sliced):", math[1:3])

print("\nMath Subject Details:")
for detail in math:
    print("-", detail)

math_topics = {"Algebra", "Geometry", "Fractions", "Decimals", "Algebra"}
science_topics = {"Plants", "Animals", "Fractions", "Matter", "Energy"}

print("\nMath topics:", math_topics)
print("Science topics:", science_topics)
print("Total Math topics:", len(math_topics))

math_topics.add("Mensuration")
math_topics.discard("Decimals")

print("\nUpdated Math topics:", math_topics)

all_topics = math_topics.union(science_topics)
common = math_topics.intersection(science_topics)
only_math = math_topics.difference(science_topics)
unique_to_each = math_topics.symmetric_difference(science_topics)

print("\nAll topics (union):", all_topics)
print("Common topics (intersection):", common)
print("Only in Math (difference):", only_math)
print("Not shared (sym. difference):", unique_to_each)