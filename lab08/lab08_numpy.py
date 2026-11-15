import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

#task 1
print(
    hours,
    hours.shape,
    hours.ndim,
    hours.size,
    hours.dtype,
    end="\n\n"
)

# task 2
print(
    hours[2],
    hours[-1],
    hours[2:6],
    hours[::2],
    hours[::-1],
    end="\n\n"
)

# # task 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(
    temperatures.shape,
    temperatures.ndim,
    temperatures.size,
    temperatures[1, 2],
    temperatures[0:2, 1:],
    temperatures[0:2, 1:3],
    sep="\n",
    end="\n\n"
)

#task 4
matrix = np.arange(1, 26).reshape(5, 5)

part1 = matrix[:3]
part2 = matrix[-2:]
part3 = matrix[:, :2]
part4 = matrix[1:4, 2:5]
part5 = matrix[3:5, 3:5]

print(
    part1, part1.shape,
    part2, part2.shape,
    part3, part3.shape,
    part4, part4.shape,
    part5, part5.shape,
    sep="\n",
    end="\n\n"
)

#task 5
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print(changed_hours, hours, sep="\n") # .copy() нужен, чтобы создать новый массив и не изменять исходный hours

changed_matrix = matrix.copy()
changed_matrix[1, 0:] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix, matrix, sep="\n", end="\n\n") # .copy() нужен, чтобы создать новый массив и не изменять исходный matrix

#task 6
numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T
print(numbers.shape, table.shape, transposed.shape) # numbers.reshape(5, 3) вызовет ошибку, так как 12 элементов не могут быть равномерно размещены в массиве размером 5x3