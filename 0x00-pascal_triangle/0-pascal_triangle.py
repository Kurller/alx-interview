def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    Returns a list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []  # Return an empty list for n <= 0

    triangle = [[1]]  # Start with the first row [1]
    for i in range(1, n):
        prev_row = triangle[i - 1]  # Get the previous row
        new_row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])  # Calculate the value using previous row's elements
        new_row.append(1)  # The last element of each row is always 1
        triangle.append(new_row)  # Append the new row to the triangle

    return triangle

