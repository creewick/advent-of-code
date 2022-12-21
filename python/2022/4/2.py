def is_overlap(start1, end1, start2, end2):
    return start1 <= start2 and start1 >= end2 or start1 >= start2 and start1 <= end2 

result = 0

with open('input.txt') as file:
    for line in file:
        s1, e1, s2, e2 = map(int, line.replace('-', ',').split(','))
        if is_overlap(s1, e1, s2, e2) or is_overlap(s2, e2, s1, e1):
            result += 1

print(result)
