def sum_of_rows(matrix):
  sums = []
  for row in matrix:
    row_sum = 0
    for element in row:
        if element is None:
            element = 0
        row_sum += element
    sums.append(row_sum)
  return sums

print(sum_of_rows([[1,2,3,4], [6,3,None,2], [-5, 9, -8, 7, 0]]))