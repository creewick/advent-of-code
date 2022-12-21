shapes = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3 }
result = 0

def get_score(shape_a, shape_b):
    if shape_a == shape_b:
        return 3
    if (shape_a + 1) % 3 == shape_b % 3:
        return 6
    return 0

with open('input.txt') as file:
    for line in file:
        a, b = line.replace('\n', '').split(' ')
        result += shapes[b] + get_score(shapes[a], shapes[b])

print(result)
