def oddCells(n: int, m: int, indices) -> int:
    matrix = []
    for i in range(n):
        matrix.append([0] * m)
    odds = 0

    for i in indices:
        for j in range(m):
            matrix[i[0]][j] += 1
            if matrix[i[0]][j] % 2 == 1:
                odds += 1
            else:
                odds -= 1
        for j in range(n):
            matrix[j][i[1]] += 1
            if matrix[j][i[1]] % 2 == 1:
                odds += 1
            else:
                odds -= 1

    return odds


n = oddCells(2, 3, [[0, 1], [1, 1]])
print(n)
