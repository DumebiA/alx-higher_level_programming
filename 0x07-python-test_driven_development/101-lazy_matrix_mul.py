#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    # Check if m_a and m_b are lists
    if not (isinstance(m_a, list) and isinstance(m_b, list)):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not (all(isinstance(row, list) for row in m_a) and all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not (m_a and m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    if not (all(isinstance(x, (int, float)) for row in m_a for x in row) and
            all(isinstance(x, (int, float)) for row in m_b for x in row)):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangles (all 'rows' have the same size)
    if not (all(len(row) == len(m_a[0]) for row in m_a) and
            all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied (columns of m_a match rows of m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

if __name__ == "__main__":
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]))

