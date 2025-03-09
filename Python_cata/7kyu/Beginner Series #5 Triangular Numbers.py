# Triangular number
# is any amount of points that can fill an equilateral triangle.
# Example: the number 6 is a triangular number
# because all sides of a triangle has the same amount of points.

def is_triangular(t):
    return (8 * t + 1) ** 0.5 % 1 == 0