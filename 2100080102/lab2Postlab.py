class FuzzySet:
    def __init__(self, elements):
        self.elements = dict(elements)

    def union(self, other):
        unionelements = dict(self.elements)
        for key, value in other.elements.items():
            if key in unionelements:
                unionelements[key] = max(unionelements[key], value)
            else:
                unionelements[key] = value
        return FuzzySet(unionelements.items())

    def intersection(self, other):
        intersectionelements = {}
        for key, value in self.elements.items():
            if key in other.elements:
                intersectionelements[key] = min(value, other.elements[key])
        return FuzzySet(intersectionelements.items())

    def __str__(self):
        return str(self.elements)


# Create the fuzzy sets
c = FuzzySet({('x1', 0.5), ('x2', 0.7), ('x3', 0.0)})
d = FuzzySet({('x1', 0.8), ('x2', 0.2), ('x3', 1.0)})

# Perform set operations
unionresult = c.union(d)
intersectionresult = c.intersection(d)

# Print the results
print("Union:", unionresult)
print("Intersection:", intersectionresult)
