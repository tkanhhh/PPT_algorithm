def divided_differences(x_values, y_values):
    n = len(x_values)
    table = [[y for y in y_values]]
    for i in range(1, n):
        next_row = []
        for j in range(n - i):
            diff = (table[i - 1][j + 1] - table[i - 1][j]) / (x_values[j + i] - x_values[j])
            next_row.append(diff)
        table.append(next_row)
    return table

def newton_interpolation(x, x_values, y_values):
    diffs = divided_differences(x_values, y_values)
    n = len(x_values)
    result = y_values[0]
    for i in range(1, n):
        term = diffs[i][0]
        for j in range(i):
            term *= (x - x_values[j])
        result += term
    return result
