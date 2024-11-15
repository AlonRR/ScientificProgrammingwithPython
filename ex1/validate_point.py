# %%
from point import Point
# Create points
p1 = Point(3, 4)
p2 = Point(1, 2)
num = 2

# String representation
print(p1)  # Should output (3,4)

# Arithmetic operations
p3 = p1 + p2  # Should create Point(4,6)
p4 = p1 - p2  # Should create Point(2,2)
p5 = p1 * 2    # Should create Point(6,8)
p6 = p1 + 1   # Should create Point(4,5)

# Indexing
x = p1[0]     # Should return 3
y = p1[1]     # Should return 4
x = p1['x']   # Should return 3
y = p1['y']   # Should return 4

# Iteration
coords = [coord for coord in p1]  # Should create list [3,4]

# Length
length = len(p1)  # Should return 2

# Distance calculation
dist = p1.distance_from_origin()  # Should return 5.0

# Equality
print(p1 == Point(3, 4))  # Should output True

