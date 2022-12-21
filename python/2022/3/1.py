scores, result = { 'a': 1, 'A': 27 }, 0

def get_priority(c):
    if ord('a') <= ord(c) <= ord('z'):
        return ord(c) - ord('a') + scores['a']
    return ord(c) - ord('A') + scores['A']

with open('input.txt') as file:
    for line in file:
        l = len(line) // 2
        for c in line[:l]:
             if c in line[l:]:
                result += get_priority(c)
                break

print(result)
