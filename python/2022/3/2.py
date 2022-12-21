scores, result, group = { 'a': 1, 'A': 27 }, 0, []

def get_priority(c):
    if ord('a') <= ord(c) <= ord('z'):
        return ord(c) - ord('a') + scores['a']
    return ord(c) - ord('A') + scores['A']

with open('input.txt') as file:
    for line in file:
        if len(group) < 3:
            group.append(line)
        if len(group) == 3:
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    result += get_priority(c)
                    break
            group = []

print(result)
