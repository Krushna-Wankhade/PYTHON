#13.	Write a Python program to generate Pascal’s triangle up to n rows, where n is given by the user.

def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        if triangle:  # If it's not the first row
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # Last element is always 1
        triangle.append(row)
    return triangle

# Get user input
n = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = generate_pascals_triangle(n)

# Print the triangle
for row in triangle:
    print(" ".join(map(str, row)).center(n * 3))
