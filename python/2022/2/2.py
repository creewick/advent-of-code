shapes, scores = { 'A': 1, 'B': 2, 'C': 3 }, { 'X': 0, 'Y': 3, 'Z': 6 }
result = 0

def get_shape(shape_a, score):
    if score == 3:
        return shape_a
    if score == 6:
        return (shape_a % 3) + 1
    return ((shape_a + 1) % 3) + 1

with open('input.txt') as file:
    for line in file:
        a, b = line.replace('\n', '').split(' ')
        result += get_shape(shapes[a], scores[b]) + scores[b]
        
print(result)
