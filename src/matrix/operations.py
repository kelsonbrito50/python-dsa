"""
Matrix Operations — 2D array problems.

Rotate: O(n²) time, O(1) space (in-place)
Spiral: O(m*n) time, O(1) space
"""


def rotate_90(matrix: list[list[int]]) -> None:
    """Rotate matrix 90° clockwise in-place. O(n²)."""
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return elements in spiral order. O(m*n)."""
    if not matrix:
        return []
    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result
