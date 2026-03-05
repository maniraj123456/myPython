"""this program demonstrates the use of sets in Python."""

seta = set()  # Create an empty set
seta.add(1)  # Add an element to the set
seta.add(2)  # Add another element to the set
print(seta)  # Output: {1, 2}

setb = set([2, 3, 4])  # Create a set with initial elements
print(setb)  # Output: {2, 3, 4}
print(seta.union(setb))  # Output: {1, 2, 3, 4} - Union of seta and setb
print(seta.intersection(setb))  # Output: {2} - Intersection of seta and setb
print(seta.difference(setb))  # Output: {1} - Elements in seta but not in setb
print(
    seta.symmetric_difference(setb)
)  # Output: {1, 3, 4} - Elements in either set but not in both
